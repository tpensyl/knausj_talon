from talon import Module, ctrl, Context, actions

mod = Module()
mod.tag("draw_box_with_sounds", desc="use pop and click to draw a box on the screen")

ctx = Context()
ctx.matches = "tag: user.draw_box_with_sounds"

@mod.action_class
class DebugWidgetActions:
    def log_mouse_coordinates():
        "log mouse coordinates"
        ctrl.mouse_pos()

    def hide_debug_box():  
        "hide the box"
        actions.user.close_widget()

    def show_debug_box():  
        "show the box"
        actions.user.set_box_widget(0, 0, 300, 100)

@ctx.action_class('user')
class DebugWidgetOverrides:
    # def init_box_widget():
    #     "override this method to create widget"
    #     print("debugwidget: there should be a box - debug.py") 
    #     actions.user.set_box_widget(0, 0, 300, 100)

    def noise_trigger_pop():
        print("debug.py:pop")
        actions.user.slow_click()
        widget = actions.user.get_widget()
        if widget:
            widget.x1, widget.y1 = ctrl.mouse_pos()
            print(widget.x1, widget.y1, widget.x2, widget.y2)
        else:
            print("debug.py:else")

    def parrot_palate():
        widget = actions.user.get_widget()
        if widget:
            widget.x2, widget.y2 = ctrl.mouse_pos()  
            print(widget.x1, widget.y1, widget.x2, widget.y2)