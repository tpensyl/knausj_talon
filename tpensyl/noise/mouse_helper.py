from talon import ctrl, Module, actions

mod = Module()

@mod.action_class
class TpensylClick:
    def slow_click():
        """Click with hold time"""
        ctrl.mouse_click(button=0, down=True)
        actions.sleep(.016)
        ctrl.mouse_click(button=0, up=True)

    def game_click(button: int = 0, times: int = 1, hold: int = None):
        """Click with hold time"""
        wait = hold
        for i in range(times):
            ctrl.mouse_click(button, hold=hold, wait=wait)

    def click_with_modifier(button: int, modifier: str, modifier_hold_time: int = "16ms"):
        """Click with modifier"""
        actions.key(modifier + ":down")
        ctrl.mouse_click(button)
        actions.sleep(modifier_hold_time)
        actions.key(modifier + ":up")

    def toggle_drag(button: int = 0):
        """Toggle drag"""
        buttons_held_down = list(ctrl.mouse_buttons_down())
        if buttons_held_down:
            for button in buttons_held_down:
                ctrl.mouse_click(button=button, up=True)
            return
        else:
            ctrl.mouse_click(button=button, down=True)