from talon import Module, actions, ctrl, Context


mod = Module()
ctx = Context()
ctx.matches = """
os: windows
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
        x=1
        print('tut unimplemented')
        pass

    # def parrot_buzz():
    #     """parrot buzz sound"""
    #     pass

    def parrot_palate():
        """parrot palate sound, has some false positives with speech"""
        actions.key("ctrl:down")
        ctrl.mouse_click(0)
        actions.key("ctrl:up")
        # actions.user.toggle_drag(0)
        pass