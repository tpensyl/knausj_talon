from talon import Module, ctrl, Context, actions, system

mod = Module()
mod.tag("draw_box_with_sounds", desc="use pop and click to draw a box on the screen")

ctx = Context()
#ctx.matches = "tag: disabled"

@mod.action_class
class DebugWidgetActions:
    def run_test_process():
        "start a process"
        # x=actions.user.system_command_nb("C:\\games\\ahk-scripts\\bstone.ahk")
        # system.launch can only rot executables, but I can't get the executable to compile  
        print("return value:  ", x)