from talon import Module, ctrl, actions
#, multiprocessing, subprocess

mod = Module()

cycle_job=None

cycle_key='up'

global_hold_ms=mod.setting("default_long_press_ms", float, default=.128)
global_wait_ms=mod.setting("default_long_wait_ms", float, default=.150)

@mod.action_class
class Actions:
    def long_press(key:str, arg_hold_ms:float=None):
        """press"""
        global global_hold_ms
        actions.key(key+':down')
        hold_ms = arg_hold_ms if arg_hold_ms else global_hold_ms.get()
        actions.sleep(hold_ms)
        actions.key(key+':up')

    def press_wait(key:str, arg_wait_ms:float=None):
        """up"""
        global global_wait_ms
        pause_ms = arg_wait_ms if arg_wait_ms else global_wait_ms.get()
        actions.user.long_press(key)
        actions.sleep(pause_ms)

    def multi_press(key:str, times:int=1, arg_wait_ms:float=None):
        """up"""
        global global_wait_ms
        pause_ms = arg_wait_ms if arg_wait_ms else global_wait_ms.get()
        for i in range(times):
            actions.user.long_press(key)
            actions.sleep(pause_ms)

    def combo_key(k1:str, k2:str, pause:float=None):
        """combo"""
        pause_ms = pause if pause else global_wait_ms.get()
        print(pause_ms)
        actions.key(k1+':down')
        actions.sleep(pause_ms)
        actions.key(k2+':down')
        actions.sleep(pause_ms)
        actions.key(k1+':up')
        actions.sleep(pause_ms)
        actions.key(k2+':up')

    def window_tab():
        """press alt tab, slowly"""
        actions.key("alt:down")
        actions.sleep("100ms")
        actions.key("tab:down")
        actions.sleep("20ms")
        actions.key("tab:up")
        actions.sleep("20ms")
        actions.key("alt:up")

    def scroll_with_modifier(mod:str, amount:float, fudge:str="10ms", times:int=1):
        """scroll while holding on a mono far key"""
        actions.key(mod+":down")
        actions.sleep(fudge)
        for x in range(times):
            actions.user.mouse_scroll_up(amount)
            actions.sleep(fudge)
        actions.key(mod+":up")

    def long_click(button:int, hold_us:str=610000):
        "hold a mouse press"
        ctrl.mouse_click(button, hold=hold_us)
