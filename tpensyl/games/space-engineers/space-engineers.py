from talon import Context, Module, actions, ctrl, cron
from time import time

mod = Module()

ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and app.name: Space Engineers
"""

LEFT_BUTTON = 0
RIGHT_BUTTON = 1

last_click_ts = time()
double_click_threshold = .5
double_pop_threshold = .3

action_map = {
    #"use_old": (lambda: actions.user.hold_until_double_press('i')),
    #"jetpack": (lambda: actions.user.long_press('space', .45)),
    "use": (lambda: use_with_double_click_drag()),
    #"jump": (lambda: actions.user.long_press('space')),
    #"drag": (lambda: actions.user.mouse_drag(0)),
    #"lunge": (lambda: actions.user.satisfactory_lunge())
}
tertiary_noise_action = action_map["use"]

@ctx.action_class('user')
class UserActions:
    def noise_trigger_pop():
        actions.user.set_hold('f', False)

        actions.user.mouse_drag_end()

        global last_click_ts
        new_click_ts = time()
        if new_click_ts - last_click_ts < double_pop_threshold:
            ctrl.mouse_click(0, down=True)
        else:
            actions.user.slow_click("16ms")
            last_click_ts = new_click_ts

    def noise_hiss_start():
        actions.user.set_hold('space', True)

    def noise_hiss_stop():
        actions.user.set_hold('space', False)

    def parrot_tut():
        #actions.user.press_wait('e') 
        #actions.key('e:down')
        #actions.user.hold_until_double_press('e')
        tertiary_noise_action()

    def parrot_palate():
        mouse_moves = ['mouse_move_down', 'mouse_move_up', 'mouse_move_left', 'mouse_move_right']
        if any([actions.user.set_hold(button, False) for button in mouse_moves]):
            return
        actions.user.toggle_hold('w', half_stop=True)

    def whistle_action(delta):
        slow_scroll(delta)

min_whistle_event_time = .35
delta_threshold = 2
delta_scaler = 15 #higher is slower
last_whistle_time = time()

def use_with_double_click_drag():
    # Close selection menu
    # if actions.user.get_hold('f'):
    #     actions.user.set_hold('f', False)
    #     return

    #actions.user.mouse_drag_end()

    global last_click_ts
    new_click_ts = time()
    if new_click_ts - last_click_ts < double_click_threshold:
        actions.user.set_hold('f', True)
    else:
        actions.user.set_hold('f', True)
        actions.user.set_hold('f', False)
        last_click_ts = new_click_ts

def slow_scroll(delta):
    global last_whistle_time
    this_whistle_time = time()
    #TODO consider using remainder instead
    delta_interval = min_whistle_event_time * delta_scaler / max(0.1, abs(delta))

    #debug_log(this_whistle_time - last_whistle_time, delta_interval, delta)

    if this_whistle_time - last_whistle_time < delta_interval:
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
    def start_destroying():
        "hold right mouse button"
        ctrl.mouse_click(button=1, down=True)

    def make_x(num:int):
        "make x items"
        n1000 = num//1000
        n100 = (num%1000)//100
        n10 = (num%100)//10
        n1 = num%10
        actions.user.game_click(times=n1, wait='32ms', hold='16ms', modifier=None, modifier_hold_time='16ms')
        actions.user.game_click(times=n10, wait='32ms', hold='16ms', modifier='ctrl', modifier_hold_time='16ms')
        actions.user.game_click(times=n100, wait='32ms', hold='16ms', modifier='shift', modifier_hold_time='16ms')
        #actions.user.game_click(times=n1000, wait='32ms', hold='16ms', modifier='ctrl-shift', modifier_hold_time='16ms')

    def set_tertiary_noise_action(action:str):
        "Set tertiary noise action"
        global tertiary_noise_action
        if action in action_map:
            tertiary_noise_action = action_map[action]


    def satisfactory_lunge():  
        "forward crouch jump"
        actions.user.set_hold('up', True)
        actions.sleep('100ms')
        actions.user.toggle_hold('c')
        actions.sleep('70ms')
        actions.user.long_press('space')
        actions.user.toggle_hold('c')

expire_job = None
def set_expire(time):
    global expire_job
    if expire_job:
        cron.cancel(expire_job)
    if time >= 0:
        expire_job = cron.after(str(time) + "s", actions.user.get_widget().close)
        cron.after(str(time) + "s", actions.user.clear_stopwatch)
        
