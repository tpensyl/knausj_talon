from talon import Context, Module, actions, ctrl, cron
from time import time

mod = Module()

ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and app.name: DSPGAME.exe
"""

last_rotate_time = time()
rotate_delta = .5
palate_action = actions.user.move_command
pop_action = actions.user.slow_click
# hiss_start_action = actions.user.start_camera_drag
# hiss_stop_action = actions.user.stop_camera_drag
hiss_start_action = lambda: actions.key("space:down") 
hiss_stop_action = lambda: actions.key("space:up") 
tut_action = actions.user.dyson_back
set_palate_mode_cron = None
@ctx.action_class('user')
class UserActions:
    def parrot_palate():
        actions.key("ctrl:up")
        palate_action()

    def noise_pop():
        actions.key("ctrl:up")
        pop_action()

    def parrot_tut():
        tut_action()

    def noise_hiss_start():
        hiss_start_action()

    def noise_hiss_stop():
        hiss_stop_action()

    def whistle_action(delta):  
        actions.mouse_scroll(by_lines=False, y=delta)
        
        global last_rotate_time
        this_rotate_time = time()
        if this_rotate_time - last_rotate_time < rotate_delta:# and False :
            return
        else:
            actions.key("r")
            last_rotate_time = this_rotate_time

@mod.action_class
class Actions:
    def queue_click():
        "shift clicks to queue actions"
        actions.user.set_hold('shift', True)
        ctrl.mouse_click(1)
        actions.sleep("15ms")
        actions.user.set_hold('shift', False)

    def add_mode():
        "temporarily make right clicks into queuing mode"
        set_palate_action(actions.user.queue_click)

    def jump_mode():
        "temporarily make right clicks into jumping mode"
        set_palate_action(lambda: actions.key('space'))

    def yeet():
        "move all items"
        actions.user.click_with_modifier(0, 'ctrl')

    def yeet_mode():
        "temporarily make right clicks into move all items"
        set_palate_action(actions.user.yeet)

    def move_mode():
        "Set pop action to move"
        global pop_action 
        pop_action = actions.user.move_command

    def click_mode():
        "Set pop action to click"
        global pop_action 
        pop_action = actions.user.slow_click  

    def move_command():
        "move the mech"
        actions.user.set_hold('shift', False)
        ctrl.mouse_click(1)

    def fast_fill():
        "pull items from a conveyor belt"
        actions.key("ctrl:down")
        ctrl.mouse_click(0, down=True)
        
    def start_camera_drag():
        "start camera drag"
        ctrl.mouse_click(button=2, down=True)

    def stop_camera_drag():
        "stop camera drag"
        ctrl.mouse_click(button=2, up=True)
    
    def dyson_back():
        "go back"
        #actions.user.set_hold('shift', False)
        actions.key("ctrl:up")
        actions.key("esc")

def reset_palate_action():
    global palate_action
    palate_action = actions.user.move_command

# TODO generalized this to work for other actions by passing a string
def set_palate_action(action):
    global palate_action
    global set_palate_mode_cron
    if set_palate_mode_cron:
        cron.cancel(set_palate_mode_cron)
        set_palate_mode_cron = None
    palate_action = action
    set_palate_mode_cron = cron.after("20s", reset_palate_action)
