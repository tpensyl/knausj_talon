from talon import Context, Module, actions, ctrl, cron, settings
from time import time

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and app.name: Borderlands 2
"""

last_click_ts = time()
double_click_threshold = .3 

last_tut_ts = time()
double_tut_threshold = .5

last_zoom_ts = time()
double_zoom_threshold = .3

zoom_out_job = None

# disable hiss while driving, as it is triggered easily by the engine noise
drive_mode_enabled = False

@mod.action_class 
class BorderlandsActions:
    def drive_mode_on():
        "Drive mode disables hiss which is otherwise too sensitive and results in constantly leaving the vehicle"
        global drive_mode_enabled
        drive_mode_enabled = True

@ctx.action_class('user')
class UserActions:
    def noise_trigger_pop():
        print("borderlands2.py.noise_trigger_pop()")
        # actions.user.toggle_hold('mouse_button_left')

        # actions.user.mouse_drag_end()
        # actions.user.set_hold('s', False)

        global last_click_ts
        new_click_ts = time()
        if new_click_ts - last_click_ts < double_click_threshold:
            print("pop:hold")
            ctrl.mouse_click(0, down=True)
        else:
            print("pop:click")
            actions.user.game_click(button=0, hold='50ms')
            last_click_ts = new_click_ts

    def parrot_palate():
        if(actions.user.set_hold('s', False)):
            return
        actions.user.toggle_hold('w', half_stop=True)
        ctrl.mouse_click(1, up=True)

    # def whistle_action(delta):
    #     slow_scroll(delta)

    def noise_trigger_hiss(active):
        
        print("drive_mode_enabled", drive_mode_enabled)
        if drive_mode_enabled:
            return # ignore this sound until drive mode is off. use tut to exit vehicle
        if active:
            # actions.mouse_scroll(by_lines=True, y=-settings.get("user.parrot_scroll_jump_size"))
            # actions.user.set_hold('w', False)
            # ctrl.mouse_click(0, up=True)
            actions.key('e:down')
        else:
            actions.key('e:up')

    def parrot_tut():
        global drive_mode_enabled
        if drive_mode_enabled:
            drive_mode_enabled = False
            actions.key('e')
            return

        # actions.user.set_hold('e', True)
        # actions.user.set_hold('e', False)
        # new_tut_ts = time()
        # if new_tut_ts - last_tut_ts < double_click_threshold:
        #     print("tut:hold")
        #     actions.user.set_hold('e', True)
        # else:
        #     print("tut:click")
        #     last_click_ts = new_tut_ts
        
        actions.key('space')

        # actions.user.toggle_hold('c') # toggle zoom

    def pedal_top_down():
        actions.user.set_hold('s', True)

    def pedal_top_up():
        actions.user.set_hold('s', False)

    def pedal_center_down():
        print("pedal_center_down")
        
        # global zoom_out_job
        # global last_zoom_ts
        # new_zoom_ts = time()
        # time_delta = new_zoom_ts - last_zoom_ts
        # last_zoom_ts = new_zoom_ts
        # if time_delta < double_zoom_threshold:
        #     if zoom_out_job:
        #         cron.cancel(zoom_out_job)
        #     return # ignore repeated key sends on peddle hold
        
        actions.user.set_hold('mouse_button_right', True)
        actions.user.set_hold('c', True)
            

    def pedal_center_up():
        print("pedal_center_up")

        global last_zoom_ts
        new_zoom_ts = time()
        time_delta = new_zoom_ts - last_zoom_ts
        last_zoom_ts = new_zoom_ts
        if time_delta < double_zoom_threshold:
            return # ignore repeated key sends on peddle hold
        
        global zoom_out_job
        zoom_out_job = cron.after("100ms", zoom_out)

    def pedal_right_down():
        actions.user.set_hold('d', True)

    def pedal_right_up():
        actions.user.set_hold('d', False)

    def pedal_left_down():
        actions.user.set_hold('a', True)

    def pedal_left_up():
        actions.user.set_hold('a', False)

def zoom_out():
    actions.user.set_hold('mouse_button_right', False)
    actions.user.set_hold('c', False)