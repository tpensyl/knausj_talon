from talon import Context, actions, ctrl, cron
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
os: windows
and win.title: /Riven.*/
"""

move_job = None
@ctx.action_class('user')
class UserActions:
    def parrot_tut():
        actions.user.toggle_drag(0)

    def parrot_palate():
        ctrl.mouse_click(0)
    
    def noise_hiss_start():
        global move_job
        move_job = cron.interval("20ms", lambda: ctrl.mouse_click(0))

    def noise_hiss_stop():
        if move_job:
            cron.cancel(move_job)