from talon import Module, ctrl, actions


mod = Module()

@mod.action_class
class NoiseActions:
    def pedal_left_down():
        """Left Pedal"""
        ctrl.mouse_click(0)
        pass

    def pedal_left_up():
        """Left Pedal"""
        # actions.mouse_release()
        pass

    def pedal_right_down():
        """Right Pedal""" 
        ctrl.mouse_click(0)
        pass

    def pedal_right_up():
        """Right Pedal""" 
        # actions.mouse_release()
        pass

    def pedal_center_down():
        """Center Pedal"""
        actions.mouse_drag()
        pass

    def pedal_center_up():
        """Center Pedal"""
        actions.mouse_release()
        pass

    def pedal_top_down():
        """Right Pedal""" 
        actions.mouse_drag()
        pass

    def pedal_top_up():
        """Right Pedal""" 
        actions.mouse_release()
        pass