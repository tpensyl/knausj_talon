from talon import Context, Module, actions

mod = Module()

# ctx = Context()
# ctx.matches = r"""
# app: chrome
# """
# ctx.tags = ['browser', 'user.tabs']

@mod.action_class
class UserActions:
    def open_okta_extension(name: str):
        """Open okta extension using plugin and hotsearch"""
        actions.key("alt-o")
        actions.sleep("400ms")
        actions.insert(name)
        actions.sleep("400ms")
        actions.key("enter")
