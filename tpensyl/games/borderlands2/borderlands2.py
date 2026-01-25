from talon import Context, Module, actions, ctrl, cron, settings
from time import time

ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and app.name: Borderlands 2
"""

last_click_ts = time()
double_click_threshold = .3

@ctx.action_class('user')
class UserActions:
    def noise_trigger_pop():
        # actions.user.toggle_hold('mouse_button_left')

        actions.user.mouse_drag_end()

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
        actions.user.toggle_hold('w', half_stop=True)

    # def whistle_action(delta):
    #     slow_scroll(delta)

    def noise_trigger_hiss(active):
        if active:
            # actions.mouse_scroll(by_lines=True, y=-settings.get("user.parrot_scroll_jump_size"))
            actions.key('e:down')
        else:
            actions.key('e:up')

    def parrot_tut():
        actions.key('e')

        