from talon import actions, Context
ctx = Context()
ctx.matches = "app.app:vscodeee and tag:disabled"

@ctx.action_class('user')
class UserActions:
    def init_box_widget():
        print("init10!") 
        actions.user.set_box_widget(100, 300, 100, 200, "99999999")
        pass