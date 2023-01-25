from talon import Module, actions, cron
from time import time
from collections import defaultdict

mod = Module()

# if the key is held down longer than this, don't use toggle
manual_toggle_min_time = .11

@mod.action_class
class Actions:
    def set_hold(key:str, new_hold_state:bool = True, halfStop:bool = False):
        "Explicitly turn hold on or off"
        set_hold(key, new_hold_state, halfStop)

    def get_hold(key:str):
        "Returned the current toggle state of a key"
        return key_is_held[key]

    def toggle_hold(key:str, halfStop:bool = False):
        "Toggle hold on and off"
        set_hold(key, not key_is_held[key], halfStop)

    def release_all_holds():
        "release all holds"
        for key in key_is_held:
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

key_mutex = defaultdict(lambda: list())
key_mutex['up'] = ['down']
key_mutex['left'] = ['right']
key_mutex['right'] = ['left']
key_mutex['down'] = ['up']
key_mutex['c'] = ['ctrl']

key_is_held = defaultdict(lambda: False)
key_hold_start_ts = {}

def toggle_hold(key):
    set_hold(key, not key_is_held[key])

def set_hold(key, new_state, halfStop = False):
    old_state = key_is_held[key]
    if (not key_is_held[key]) and new_state == True:
        key_hold_start_ts[key] = time()

    if old_state == False and new_state == True:
        for incompatible_key in key_mutex[key]:
            # Preempt infinite loops
            if not(incompatible_key == key) and key_is_held[incompatible_key]:
                set_hold(incompatible_key, False)
                if halfStop:
                    return
        actions.key(key+':down')
    elif old_state == True and new_state == False: 
        # Doing :up carelessly leads to repeated key press during a hold
        actions.key(key+':up')

    key_is_held[key] = new_state

    
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
