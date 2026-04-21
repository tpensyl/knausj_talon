from talon import Module, actions, ctrl, Context


mod = Module()
ctx = Context()
ctx.matches = """
os: mac
"""


@ctx.action_class('user')
class NoiseActions:

    # def noise_trigger_pop():
    #     actions.user.game_click(button=0, hold='50ms')

    # def noise_trigger_hiss(active):
    #     if active:
    #         actions.mouse_drag(2)
    #     else:
    #         actions.mouse_release(2)

    # def pedal_center_down():
    #     actions.mouse_drag(2)

    # def pedal_center_up():
    #     actions.mouse_release(2)

    # def pedal_top_down():
    #     actions.mouse_drag(0)

    # def pedal_top_up():
    #     actions.mouse_release(0)

    def pedal_right_down():
        actions.speech.enable()

    def pedal_right_up():
        actions.speech.disable()

    # def pedal_left_down():
        # actions.user.game_click(button=0, hold='50ms')

    # def noise_trigger_pop():
    #     pass

    # def noise_hiss_start():
    #     """Invoked when the user starts hissing (potentially while speaking)"""
    #     # print("noise_linux.py:hiss disabled")
    #     pass

    # def noise_hiss_stop():
    #     """Invoked when the user finishes hissing (potentially while speaking)"""
    #     pass

    # # had to drop the power way down on linuxb/shure
    # def parrot_tut():
    #     """parrot tut sound"""
    #     actions.tracking.control_toggle()
    #     pass

    # def parrot_buzz():
    #     """parrot buzz sound"""
    #     pass

    # def parrot_palate():
    #     """parrot palate sound, has some false positives with speech"""
    #     actions.key("ctrl:down")
    #     ctrl.mouse_click(0)
    #     actions.key("ctrl:up")
    #     pass