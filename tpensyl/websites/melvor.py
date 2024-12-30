from talon import Context, ctrl, actions

ctx = Context()
ctx.matches = r"""
win.title: /.*Melvor Idle.*/
"""
# on laptop screen with bottom right of map align with bottom right of screen, falls zoom` out
hex1=(757, 691)
hex2=(1830, 994)
close_event=(964, 729)
travel_button=(524, 973)
ping=True

# @ctx.action_class("user")
# class UserActions:
#     def parrot_palate():
#         ctrl.mouse_click(0)
#         print(ctrl.mouse_pos())
#         # actions.user.mouse_remote_click(*close_event)

    # def noise_trigger_pop():
    #     global ping
    #     for i in range(1, -1):
    #         target = hex1 if ping else hex2
    #         ping = not ping
    #         actions.user.mouse_remote_click(*target)
    #         actions.sleep("10ms")
    #         actions.user.mouse_remote_click(*travel_button)
    #         actions.sleep("30ms")
    #         actions.user.mouse_remote_click(*close_event)
    #         actions.sleep("30ms")


        
