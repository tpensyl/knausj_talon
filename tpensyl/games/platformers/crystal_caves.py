from talon import Context, actions
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and win.title: /Crystal Caves HD/
"""

@ctx.action_class("user")
class UserActions:
    def noise_trigger_pop():
        # For menu navigation
        move_left()
        # actions.key("enter")

    def noise_hiss_start():
        jump()

    def noise_hiss_stop():
        return

    def parrot_palate():
        move_right()

    def parrot_tut():
        # Remapped fire from alt to space, to allow for safe alt+tab
        actions.user.long_press("space")
        
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

def jump():
    actions.user.long_press("ctrl")