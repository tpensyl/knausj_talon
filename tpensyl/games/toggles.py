from talon import Module, actions, cron
from time import time
from collections import defaultdict

mod = Module()

# if the key is held down longer than this, don't use toggle
manual_toggle_min_time = .11

# px/s  Can be changed dynamically via setter
mouse_move_speed = 100

@mod.action_class
class Actions:
    def set_hold(key:str, new_hold_state:bool = True, half_stop:bool = False):
        "Explicitly turn hold on or off"
        return set_hold(key, new_hold_state, half_stop)

    def get_hold(key:str):
        "Returned the current toggle state of a key"
        return key_is_held[key]

    def toggle_hold(key:str, half_stop:bool = False):
        "Toggle hold on and off"
        set_hold(key, not key_is_held[key], half_stop)

    def release_all_holds(exclude:list=[]):
        "release all holds"
        for key in key_is_held:
            if key in exclude:
                continue
            if key_is_held[key]:
                set_hold(key, False)

    def end_long_toggle(key:str):
        "Disable hold only if it's been on for awhile"
        if time() >= key_hold_start_ts[key] + manual_toggle_min_time:
            set_hold(key, False)

    def hold_until_double_press(key:str):
        "Rapid triggering results in a single press and hold"
        hold_until_double_press(key)

    def hold_on_double_press_down(key:str):
        "Rapid triggering results in a hold on the second press"
        hold_on_double_press_down(key)

    def hold_on_double_press_up(key:str):
        "Release unless a hold was just triggered"
        hold_on_double_press_up(key)

    def set_toggle_mouse_speed(speed:int):
        "Speed for mouse move toggles"
        global mouse_move_speed
        mouse_move_speed = speed


MOUSE_MOVE_UP = "mouse_move_up"
MOUSE_MOVE_DOWN = "mouse_move_down"
MOUSE_MOVE_LEFT = "mouse_move_left"
MOUSE_MOVE_RIGHT = "mouse_move_right"
key_mutex = defaultdict(lambda: list())
key_mutex['up'] = ['down', MOUSE_MOVE_UP, MOUSE_MOVE_DOWN, 
                   MOUSE_MOVE_LEFT, MOUSE_MOVE_RIGHT]
key_mutex['left'] = ['right']
key_mutex['right'] = ['left']
key_mutex['down'] = ['up']
key_mutex['w'] = ['s']
key_mutex['a'] = ['d']
key_mutex['d'] = ['a']
key_mutex['s'] = ['w']
key_mutex['c'] = ['ctrl']
key_mutex[MOUSE_MOVE_UP] = [MOUSE_MOVE_DOWN]
key_mutex[MOUSE_MOVE_DOWN] = [MOUSE_MOVE_UP]
key_mutex[MOUSE_MOVE_LEFT] = [MOUSE_MOVE_RIGHT]
key_mutex[MOUSE_MOVE_RIGHT] = [MOUSE_MOVE_LEFT]

key_is_held = defaultdict(lambda: False)
key_hold_start_ts = {}

def toggle_hold(key):
    set_hold(key, not key_is_held[key])

# Return true if operation changes the state, including partial mutex.
def set_hold(key, new_state, half_stop = False, respect_mutex = True):
    old_state = key_is_held[key]
    key_is_held[key] = new_state
    
    if not old_state and new_state == True:
        key_hold_start_ts[key] = time()

    if old_state == False and new_state == True:
        if respect_mutex:
            for incompatible_key in key_mutex[key]:
                if key_is_held[incompatible_key]:
                    set_hold(incompatible_key, False, False)
                    if half_stop:
                        return True
        key_down(key)
    elif old_state == True and new_state == False: 
        # Doing :up carelessly leads to repeated key press during a hold
        key_up(key)

    state_changed = (old_state != new_state)
    return state_changed

keys_this_down = {}
keys_last_down = {}
double_press_threshold = .2
def hold_on_double_press_up(key):
    last_up = keys_last_down.get(key, 0)
    this_up = time()
    if this_up - last_up > double_press_threshold:
        set_hold(key, False)
    else:
        #something is broken
        print("leaving key [" + key + "] pressed due to rapid press")
    keys_last_down[key] = keys_this_down[key]

def hold_on_double_press_down(key):
    keys_this_down[key] = time()
    set_hold(key, True)

# Double press is drag, without releasing the first press
# This means the key is not released until the wait time.
keys_release_job = {}
double_click_wait_time = "300ms"
def hold_until_double_press(key):
    def finish_press():
        print("up")
        key_up(key)
        del(keys_release_job[key])
        
    if key in keys_release_job:
        print("hold")
        # leave held down
        cron.cancel(keys_release_job[key])
        del(keys_release_job[key])
    else:
        print("down")
        key_down(key)
        keys_release_job[key] = cron.after(double_click_wait_time, finish_press)

def key_down(key):
    if key == MOUSE_MOVE_UP:
        actions.user.start_mouse_move_down(-mouse_move_speed)
    elif key == MOUSE_MOVE_DOWN:
        actions.user.start_mouse_move_down(mouse_move_speed)
    elif key == MOUSE_MOVE_LEFT:
        actions.user.start_mouse_move_right(-mouse_move_speed)
    elif key == MOUSE_MOVE_RIGHT:
        actions.user.start_mouse_move_right(mouse_move_speed)
    else:
        actions.key(key+':down')

def key_up(key):
    if key in [MOUSE_MOVE_UP, MOUSE_MOVE_DOWN, MOUSE_MOVE_LEFT, MOUSE_MOVE_RIGHT]:
        actions.user.stop_mouse_move()
    else:
        actions.key(key+':up')