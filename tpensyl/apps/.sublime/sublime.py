from talon import Context, actions
ctx = Context()
ctx.matches = r"""
app: sublime
"""
#ctx.tags = ['browser', 'user.tabs']

@ctx.action_class('app')
class AppActions:
    def tab_close():    actions.key('ctrl-f4')
    def tab_next():     actions.key('ctrl-pagedown')
    def tab_previous(): actions.key('ctrl-pageup')
    def tab_reopen():   actions.key('ctrl-shift-t')
    def tab_open():     actions.key('ctrl-n')

@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        if number < 90:
            actions.key(f"alt-{number}")

    def tab_final():
        actions.key("alt-9")


# @ctx.action_class('user')
# class NoiseActions:
#     def parrot_palate():
#         """parrot palate sound, has some false positives with speech"""
#         pass