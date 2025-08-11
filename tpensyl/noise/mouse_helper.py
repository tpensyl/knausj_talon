from talon import ctrl, Module, actions, cron

mod = Module()

global mouse_rest_interrupt
mouse_rest_interrupt = False

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

    def toggle_drag(button : int = 0):
        """Toggle drag"""
        buttons_held_down = list(ctrl.mouse_buttons_down())
        if buttons_held_down:
            for button_down in buttons_held_down:
                ctrl.mouse_click(button=button_down, up=True)
            return
        else:
            ctrl.mouse_click(button=button, down=True)

    def mouse_rest(duration_ms : int = 1500):
        """Effectively ignore mouse movements for short duration, or until explicitly interrupted"""
        global mouse_rest_interrupt
        mouse_rest_interrupt = False
        do_mouse_rest(duration_ms, ctrl.mouse_pos())

    def interrupt_mouse_rest() -> bool:
        """Terminate a mouse rest. Early"""
        global mouse_rest_interrupt
        if mouse_rest_interrupt == False:
            print("interrupted mouse rest")
            mouse_rest_interrupt = True
            return True
        else:
            return False

    def mouse_move(dx : int = 0, dy : int = 0):
        """Perform relative mouse movement"""
        pos = ctrl.mouse_pos() 
        new_pos = (pos[0] + dx, pos[1] + dy)
        ctrl.mouse_move(*new_pos)

    def mouse_remote_click(x : int, y : int, delay: str = "1ms"):
        """Click a remote position without moving the mouse"""
        pos = ctrl.mouse_pos()
        ctrl.mouse_move(x, y)
        ctrl.mouse_click(0)
        actions.sleep(delay)
        ctrl.mouse_move(*pos)

def do_mouse_rest(duration_ms, position):
    global mouse_rest_interrupt
    ctrl.mouse_move(*position)
    if duration_ms > 0 and mouse_rest_interrupt == False:
        cron.after("10ms", lambda: do_mouse_rest(duration_ms - 10, position))
    else:
        mouse_rest_interrupt = False

def to_ms(time_str):
    if not time_str:
        return 0
    if time_str[-2:] == 'ms':
        return int(time_str[:-2])*1000
    if time_str[-1:] == 's':
        return int(time_str[:-1])*1000*1000
    