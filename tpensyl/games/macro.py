from talon import Module, ctrl, actions, cron
import time
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
        time.sleep(hold_ms)
        actions.key(key+':up')

    def press_wait(key:str, arg_wait_ms:float=None):
        """up"""
        global global_wait_ms
        pause_ms = arg_wait_ms if arg_wait_ms else global_wait_ms.get()
        actions.user.long_press(key)
        time.sleep(pause_ms)

    def multi_press(key:str, times:int=1, arg_wait_ms:float=None):
        """up"""
        global global_wait_ms
        pause_ms = arg_wait_ms if arg_wait_ms else global_wait_ms.get()
        for i in range(times):
            actions.user.long_press(key)
            time.sleep(pause_ms)

    def combo_key(k1:str, k2:str, pause:float=None):
        """combo"""
        pause_ms = pause if pause else global_wait_ms.get()
        print(pause_ms)
        actions.key(k1+':down')
        time.sleep(pause_ms)
        actions.key(k2+':down')
        time.sleep(pause_ms)
        actions.key(k1+':up')
        time.sleep(pause_ms)
        actions.key(k2+':up')

    #def window_tab(number_small: int):
    def window_tab():
        """press alt tab"""
        actions.key("alt:down")
        actions.sleep("100ms")
        # actions.key(f"tab:{number_small}")
        actions.key("tab")
        actions.sleep("100ms")
        actions.key("alt:up")
