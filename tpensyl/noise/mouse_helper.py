from talon import ctrl, Module, actions

mod = Module()

@mod.action_class
class TpensylClick:
    def slow_click(delay_s: str = "16ms"):
        """Click with hold time"""
        ctrl.mouse_click(button=0, down=True)
        actions.sleep(delay_s)
        ctrl.mouse_click(button=0, up=True)
        actions.sleep(delay_s)

    def game_click(button: int = 0, 
                   times: int = 1, 
                   wait: str = None,
                   hold: str = None, 
                   modifier: str = None, 
                   modifier_hold_time: str = None):
        """Fully customizable click"""
        print("hello world")
        for _ in range(times):
            print(button, to_ms(hold), wait,to_ms(wait)-to_ms(modifier_hold_time), times, modifier)
            if modifier:
                actions.key(modifier + ":down")
                actions.sleep(modifier_hold_time)
            ctrl.mouse_click(button, hold=to_ms(hold), wait=to_ms(wait)-to_ms(modifier_hold_time), times=times)
            if modifier:
                actions.sleep(modifier_hold_time)
                actions.key(modifier + ":up")

    def click_with_modifier(button: int, modifier: str, modifier_hold_time: str = "16ms"): 
        """Click with modifier"""
        if modifier:
            actions.key(modifier + ":down")
            actions.sleep(modifier_hold_time)
        ctrl.mouse_click(button)
        if modifier:
            actions.sleep(modifier_hold_time)
            actions.key(modifier + ":up")

    def click_with_modifier(button: int, modifier: str, modifier_hold_time: str = "16ms"): 
        """Click with modifier"""
        print(modifier_hold_time)
        actions.key(modifier + ":down")
        actions.sleep(modifier_hold_time)
        ctrl.mouse_click(button, hold=32000)
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

def to_ms(time_str):
    if not time_str:
        return 0
    if time_str[-2:] == 'ms':
        return int(time_str[:-2])*1000
    if time_str[-1:] == 's':
        return int(time_str[:-1])*1000*1000
    