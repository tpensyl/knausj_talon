from talon import Module, actions, Context


mod = Module()
ctx = Context()
ctx.matches = """
app.exe: flashplayer_29_gemcraft.exe
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
        actions.user.toggle_hold('shift')
        pass

    def parrot_palate():
        """parrot palate sound, has some false positives with speech"""
        actions.user.toggle_drag(0)
        pass