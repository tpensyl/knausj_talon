from talon import Context, actions

ctx = Context()
ctx.matches = r"""
win.title: /Railroad Tycoon II.*/
"""
@ctx.action_class('user')
class UserActions:
    def noise_pop():
        actions.user.mouse_drag_end()
        actions.user.game_click(0, times=1, hold=16000)

    def noise_hiss_start():
        # cancel last drag for convenience
        actions.key('s')
        actions.key('t')
        actions.user.mouse_drag(0)

    def noise_hiss_stop():
        return
        #pop to stop drag
