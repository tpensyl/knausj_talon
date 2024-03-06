from talon import Module, actions, ctrl, Context


mod = Module()
ctx = Context()
ctx.matches = """
os: linux
"""


@ctx.action_class('user')
class NoiseActions:
    # def noise_trigger_pop():
    #     pass

    # def noise_hiss_start():
    #     """Invoked when the user starts hissing (potentially while speaking)"""
    #     pass

    # def noise_hiss_stop():
    #     """Invoked when the user finishes hissing (potentially while speaking)"""
    #     pass

    def parrot_tut():
        """parrot tut sound"""
        pass
        # would be nice ut tut doesn't seem to be working on my linux machine and microphone
        # actions.toggle_drag()

    # def parrot_buzz():
    #     """parrot buzz sound"""
    #     pass

    def parrot_palate():
        """parrot palate sound, has some false positives with speech"""
        actions.key("ctrl:down")
        ctrl.mouse_click(0)
        actions.key("ctrl:up")
        pass