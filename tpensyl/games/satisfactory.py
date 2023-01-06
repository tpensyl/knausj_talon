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
        actions.user.set_autorun(True)

    def noise_hiss_stop():
        actions.user.set_autorun(False)

    def parrot_tut():
        #actions.user.press_wait('e') 
        #actions.key('e:down')
        #actions.user.toggle_hold_on_double_press('e')
        tertiary_noise_action()

    def parrot_palate():
        actions.user.toggle_autorun()

    def whistle_action(delta):
        slow_scroll(delta)

def slow_scroll(delta):
    global last_whistle_time
    this_whistle_time = time()
    if this_whistle_time - last_whistle_time < min_whistle_event_time:
        return
    else:
        if delta < -delta_threshold:
            actions.mouse_scroll(by_lines=True, y=-10)
        elif delta > delta_threshold:
            actions.mouse_scroll(by_lines=True, y=10)
        last_whistle_time = this_whistle_time

min_whistle_event_time = .35
delta_threshold = 2
last_whistle_time = time()
currently_moving = False
autorun_start_time = time()

# if the run button is held down longer than this, don't use autorun
manual_autorun_min_time = .11

action_map = {
    "use": (lambda: actions.user.toggle_hold_on_double_press('e')), 
    "jump": (lambda: actions.user.long_press('space'))
}
tertiary_noise_action = action_map["use"]

@mod.action_class
class Actions:
    def set_tertiary_noise_action(action:str):
        "Set tertiary noise action"
        global tertiary_noise_action
        if action in action_map:
            print("==========SET", action, action_map[action])
            tertiary_noise_action = action_map[action]

    def set_autorun(new_moving_state:bool):
        "Explicitly turn autorun on or off"
        update_autorun(new_moving_state)

    def toggle_autorun():
        "Toggle autorun on and off"
        global currently_moving
        update_autorun(not currently_moving)

    def end_long_autorun():
        "Disable autorun only if it's been on for awhile"
        global currently_moving, autorun_start_ts
        elapsed_time = time() - autorun_start_ts
        if elapsed_time >= manual_autorun_min_time:
            update_autorun(False)

    def toggle_hold(key:str):
        "Allow holding of various keys"
        toggle_hold(key)

    def toggle_hold_on_double_press(key:str):
        "Allow holding of various keys"
        # hold_on_double_press(key)
        hold_until_double_press(key)

def update_autorun(state = None, toggle = False):
    global currently_moving, autorun_start_ts
    if toggle:
        new_state = not currently_moving
    elif state is not None:
        new_state = state
    else:
        raise ValueError("state must be specified if toggle is false")

    if not currently_moving and new_state == True:
        autorun_start_ts = time()
        
    currently_moving = new_state
    if currently_moving:
        actions.key('up:down')
    else:
        actions.key('up:up')


keys_down = {}
keys_last_press = {}

def toggle_hold(key):
    if key in keys_down:
        actions.key(key+':up')
        del(keys_down[key])
    else:
        actions.key(key+':down')
        keys_down[key] = True

def hold_on_double_press(key):
    print('toggle', key)
    if key in keys_down:
        print('up', key)
        actions.key(key+':up')
        del(keys_down[key])
        #return

    last_press = keys_last_press.get(key, 0)
    this_press = time()
    print(this_press - last_press)
    if this_press - last_press < double_click_threshold:
        actions.key(key+':down')
        keys_down[key] = True
    else:
        actions.user.long_press(key)
    keys_last_press[key] = this_press

# Double press is drag, without releasing the first press
# This means the key is not released until the wait time.
keys_release_job = {}
double_click_wait_time = "300ms"
def hold_until_double_press(key):
    def finish_press():
        print("up")
        actions.key(key+':up')
        del(keys_release_job[key])
        
    if key in keys_release_job:
        print("hold")
        # leave held down
        cron.cancel(keys_release_job[key])
        del(keys_release_job[key])
    else:
        print("down")
        actions.key(key+':down')
        keys_release_job[key] = cron.after(double_click_wait_time, finish_press)

# def cron_replace(delay, f):
#     global stop_job
#     if stop_job:
#         cron.cancel(stop_job)
#     stop_job = cron.after(delay, f) 
