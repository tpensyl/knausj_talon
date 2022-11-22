from talon import Context, actions
ctx = Context()

@ctx.action_class('user')
class UserActions:
    def noise_pop():
        actions.user.slow_click()
