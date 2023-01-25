from talon import Context, Module, actions, ctrl, cron
from time import time

mod = Module()

ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and app.name: Satisfactory
"""

LEFT_BUTTON = 0
RIGHT_BUTTON = 1

last_click_ts = time()
double_click_threshold = .5
double_click_threshold = .35

action_map = {
    "use_old": (lambda: actions.user.hold_until_double_press('i')),
    "use": (lambda: actions.user.long_press('i')),
    "jump": (lambda: actions.user.long_press('space'))
}
tertiary_noise_action = action_map["use"]

@ctx.action_class('user')
class UserActions:
    def noise_pop():
        # Close selection menu
        if actions.user.get_hold('i'):
            actions.user.set_hold('i', False)
            return

        actions.user.mouse_drag_end()

        global last_click_ts
        new_click_ts = time()
        if new_click_ts - last_click_ts < double_click_threshold:
            ctrl.mouse_click(0, down=True)
        else:
            ctrl.mouse_click(0)
        last_click_ts = new_click_ts

    def noise_hiss_start():
        actions.user.set_hold('up', True)

    def noise_hiss_stop():
        actions.user.set_hold('up', False)

    def parrot_tut():
        #actions.user.press_wait('e') 
        #actions.key('e:down')
        #actions.user.hold_until_double_press('e')
        tertiary_noise_action()

    def parrot_palate():
        actions.user.toggle_hold('up', halfStop=True)

    def whistle_action(delta):
        slow_scroll(delta)

    def init_box_widget():
        #block_compass()
        noop = None

min_whistle_event_time = .35
delta_threshold = 2
delta_scaler = 15 #higher is slower
last_whistle_time = time()

def slow_scroll(delta):
    global last_whistle_time
    this_whistle_time = time()
    #TODO consider using remainder instead
    delta_interval = min_whistle_event_time * delta_scaler / max(0.1, abs(delta))

    #debug_log(this_whistle_time - last_whistle_time, delta_interval, delta)

    if this_whistle_time - last_whistle_time < delta_interval:# and False :
        return
    else:
        print("rotate")
        if delta < -delta_threshold:
            print("scroll down")
            actions.mouse_scroll(by_lines=True, y=-10)
            last_whistle_time = this_whistle_time
        elif delta > delta_threshold:
            actions.mouse_scroll(by_lines=True, y=10)
            last_whistle_time = this_whistle_time

def debug_log(*args):
    text = ', '.join(map(lambda x: str(int(1000*x)/1000), args))
    actions.user.set_debug_text(text)

@mod.action_class
class Actions:
    def set_tertiary_noise_action(action:str):
        "Set tertiary noise action"
        global tertiary_noise_action
        if action in action_map:
            print("==========SET", action, action_map[action])
            tertiary_noise_action = action_map[action]

    def block_compass():
        "Block compass temporarily, to make scans more opaque"
        block_compass()
        cron.after("46s", actions.user.get_widget().close)

    def satisfactory_back():
        "complex back command"
        #if actions.user.get_hold('up'):
        #    actions.user.set_hold('up', False)
        actions.user.mouse_drag_end()
        released_at_least_one_key = False
        for key in ('down', 'left', 'right', 'i'):
            if actions.user.get_hold(key):
                print(key, 'back releasing')
                actions.user.set_hold(key, False)
                released_at_least_one_key = True
        actions.user.release_all_holds()
        if not released_at_least_one_key:
            actions.key('esc')

def satisfactory_key_release():  
    actions.key('ctrl:up')
    actions.key('shift:up')
    actions.key('alt:up')
    actions.key('i:up')

def block_compass():
    # actions.user.set_box_widget(620, 0, 1310, 135, "000000ff")
    actions.user.set_box_widget(400, -1, 1500, 200, "000000ff")