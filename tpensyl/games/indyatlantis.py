from talon import Context, Module, actions, ctrl, cron
ctx = Context()
ctx.matches = r"""
#mode: user.gameboy
win.title: /Indiana Jones and the Fate of Atlantis/
"""

@ctx.action_class('user')
class UserActions:
    def noise_pop():
        actions.key('.')
        ctrl.mouse_click(0)
    def noise_hiss_start():
        #actions.user.indy_skip()
        print('hi')
        # actions.key('esc')
        # actions.key('.')
        actions.user.start_indy_loop()
    def noise_hiss_stop():
        actions.user.stop_indy_loop()

mod = Module()
global indy_loop_cron
indy_loop_cron=None

@mod.action_class
class Actions:
    def start_indy_loop(interval_s:float=.2):
        """Start button loop"""
        global indy_loop_cron
        if not indy_loop_cron:
            indy_loop_cron = cron.interval(str(int(interval_s*1000)) + "ms", actions.user.indy_skip)

    def stop_indy_loop():
        """Stop button loop"""
        global indy_loop_cron
        if indy_loop_cron:
            cron.cancel(indy_loop_cron)
            indy_loop_cron = None

    def indy_skip(hold_time:float=.016):
        """cancel/skip"""
        print("indy skip")
        actions.key('esc')
        actions.key('.')
