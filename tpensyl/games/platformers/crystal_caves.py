from talon import Context, actions
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and win.title: /Crystal Caves HD/
"""

global last_dir
last_dir = "left"

@ctx.action_class("user")
class UserActions:
    def noise_trigger_pop():
        # For menu navigation
        #move_left()
        #actions.key("enter")
        #fire()
        pass

    def noise_hiss_start():
        actions.user.long_press(last_dir, arg_hold_ms=.020)

    def noise_hiss_stop():
        #actions.key(last_dir + ":up")
        pass

    def parrot_palate():
        jump()

    def parrot_tut():
        fire()

    def pedal_left_down():
        global last_dir
        last_dir = 'left'
        actions.key('left:down')

    def pedal_left_up():
        actions.key('left:up')

    def pedal_right_down():
        global last_dir
        last_dir = 'right'
        actions.key('right:down')

    def pedal_right_up():
        actions.key('right:up')

# unused idea for holding left right movement. using real pedal holds instead        
moving_left = False
moving_right = False

def move_left():
    global moving_left, moving_right
    if moving_right:
        actions.key("right:up")
        moving_right = False
    if not moving_left:
        actions.key("left:down")
        moving_left = True
    else:
        actions.key("left:up")
        moving_left = False

def move_right():
    global moving_left, moving_right
    if moving_left:
        actions.key("left:up")
        moving_left = False
    if not moving_right:
        actions.key("right:down")
        moving_right = True
    else:
        actions.key("right:up")
        moving_right = False

# Remapped jump from ctrl, which played poorly with the virtual f-keys used by peddle
def jump():
    actions.user.long_press("j")

# Remapped fire from alt to space, to allow for safe alt+tab
def fire():
    actions.user.long_press("space")