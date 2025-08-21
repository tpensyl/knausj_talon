from talon import Context, Module, actions

mod = Module()

ctx_mac = Context()
ctx_mac.matches = r"""
os: mac
"""
# ctx_mac.tags = ['browser', 'user.tabs']

@mod.action_class
class Actions:
    def open_okta_extension(name: str):
        """Open okta extension using plugin and hotsearch"""
        # print("default okta action")
        # actions.key("alt-o")
        # if name:
        #     actions.sleep("400ms")
        #     actions.insert(name)
        #     actions.sleep("400ms")
        #     actions.key("enter")

@ctx_mac.action_class("user")
class MacActions:
    def open_okta_extension(name: str):
        print("mac okta action")
        actions.key("shift-cmd-o")
        if name:
            actions.sleep("200ms")
            actions.insert(name)
            actions.sleep("200ms")
            actions.key("enter")
