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
break_loop = False

# @ctx.action_class("user")
# class UserActions:
#     def parrot_palate():
#         global break_loop
#         break_loop = True
#
#     def noise_trigger_pop():
#         global ping
#         global break_loop
#         break_loop = False
#         for i in range(1, 10000):
#             if break_loop:
#                 return
#             target = hex1 if ping else hex2
#             ping = not ping
#             actions.user.mouse_remote_click(*target)
#             actions.sleep("30ms")
#             actions.user.mouse_remote_click(*travel_button)
#             actions.sleep("90ms")
#             actions.user.mouse_remote_click(*close_event)
#             actions.sleep("90ms")


        
