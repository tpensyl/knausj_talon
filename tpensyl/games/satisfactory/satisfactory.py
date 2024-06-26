from talon import Context, Module, actions, ctrl, cron
from time import time

mod = Module()

ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and app.name: FactoryGame
"""

LEFT_BUTTON = 0
RIGHT_BUTTON = 1

last_click_ts = time()
double_click_threshold = .5
double_click_threshold = .3

action_map = {
    "use": (lambda: actions.user.hold_until_double_press('e')),
    "jetpack": (lambda: actions.user.long_press('space', .45)),
    "use_new": (lambda: actions.user.long_press('e')),
    "jump": (lambda: actions.user.long_press('space')),
    "drag": (lambda: actions.user.mouse_drag(0)),
    "lunge": (lambda: actions.user.satisfactory_lunge())
}
tertiary_noise_action = action_map["use"]

@ctx.action_class('user')
class UserActions:
    def noise_trigger_pop():
        # Close selection menu
        if actions.user.get_hold('e'):
            actions.user.set_hold('e', False)
            return

        actions.user.mouse_drag_end()

        global last_click_ts
        new_click_ts = time()
        if new_click_ts - last_click_ts < double_click_threshold:
            ctrl.mouse_click(0, down=True)
        else:
            # ctrl.mouse_click(0)
            actions.user.game_click(button=0, hold='50ms')
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
        print(mouse_moves)
        actions.user.toggle_hold('w', half_stop=True)

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
    def set_tertiary_noise_action(action:str):
        "Set tertiary noise action"
        global tertiary_noise_action
        if action in action_map:
            tertiary_noise_action = action_map[action]

    def block_scan(time:int = -1):
        "Give positive argument to block compass plus scan bubbles"
        actions.user.set_box_widget(400, -1, 1500, 200, "000000ff")
        set_expire(time)

    def block_compass(time:int = -1):
        "Give positive argument to block compass"
        # Before I discovered you can turn off the icons
        # actions.user.set_box_widget(690, 20, 1244, 131, "000000ff")
        actions.user.set_box_widget(696, 23, 1232, 38, "000000ff")
        set_expire(time)

    def satisfactory_back():
        "complex back command"
        #if actions.user.get_hold('up'):
        #    actions.user.set_hold('up', False)
        released_at_least_one_key = False
        for key in ('s', 'a', 'd', 'i'):
            if actions.user.get_hold(key):
                print(key, 'back releasing')
                actions.user.set_hold(key, False)
                released_at_least_one_key = True
        actions.user.release_all_holds(exclude=['w'])
        if not released_at_least_one_key:
            actions.user.long_press('esc')
            # actions.key('esc')

    def satisfactory_drop():  
        "drag the hovered item from inventory onto the ground"
        ORIGINAL_MOUSE_POSITION = ctrl.mouse_pos()
        OUT_OF_INVENTORY = 100, 100

        actions.user.release_all_holds()
        ctrl.mouse_click(button=0, down=True)
        actions.user.mouse_move_smooth(*OUT_OF_INVENTORY, 3, 64)
        ctrl.mouse_click(button=0, up=True)
        # actions.sleep('l56ms')
        ctrl.mouse_move(*ORIGINAL_MOUSE_POSITION)

    def satisfactory_click():  
        "click specific location, returning the cursor afterward"
        ORIGINAL_MOUSE_POSITION = ctrl.mouse_pos()
        TARGET = 100, 100

        actions.user.mouse_move_smooth(*TARGET, 3, 64)
        ctrl.mouse_click(button=0)
        actions.user.mouse_move_smooth(*ORIGINAL_MOUSE_POSITION, 3, 64)

    def satisfactory_lunge():  
        "forward crouch jump"
        actions.user.set_hold('w', True)
        actions.sleep('200ms')
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
        
