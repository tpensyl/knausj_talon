from talon import Context, Module, actions, ctrl, cron
from time import time

mod = Module()
ctx = Context()

ctx.matches = r"""
app.name: Satisfactory
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
        # Release drag if dragging
        buttons_held_down = list(ctrl.mouse_buttons_down())
        if LEFT_BUTTON in buttons_held_down:
            ctrl.mouse_click(button=LEFT_BUTTON, up=True)
            #return

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
        actions.user.toggle_hold('up')

    def whistle_action(delta):
        slow_scroll(delta)

min_whistle_event_time = .35
delta_threshold = 2
delta_scaler = 15 #higher is slower
last_whistle_time = time()

def slow_scroll(delta):
    global last_whistle_time
    this_whistle_time = time()
    #TODO consider using remainder instead
    delta_interval = min_whistle_event_time * delta_scaler / max(0.1, abs(delta))

    debug_log(this_whistle_time - last_whistle_time, delta_interval, delta)

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
