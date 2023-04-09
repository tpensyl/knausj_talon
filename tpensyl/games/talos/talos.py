from talon import Context, Module, actions, ctrl, cron
from time import time

mod = Module()

ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and app.name: Talos
"""

@ctx.action_class('user')
class UserActions:
    def noise_pop():
        ctrl.mouse_click(0)

    def noise_hiss_start():
        actions.user.set_hold('space', True)

    def noise_hiss_stop():
        actions.user.set_hold('space', False)

    def parrot_tut():
        ctrl.mouse_click(1)

    def parrot_palate():
        print("talos palate")
        actions.user.toggle_hold('up', half_stop=True)

    def whistle_action(delta):
        x=1
        #actions.mouse_scroll(by_lines=True, y=-10*delta)

action_map = {
    "alt-use": (lambda: ctrl.mouse_click(1)),
    "jump": (lambda: actions.key('space')),
    "drag": (lambda: actions.user.mouse_drag(0))
}
tertiary_noise_action = action_map["jump"]

@mod.action_class
class Actions:
    def set_talos_tertiary_noise_action(action:str):
        "Set tertiary noise action"
        global tertiary_noise_action
        if action in action_map:
            print("==========SET", action, action_map[action])
            tertiary_noise_action = action_map[action]