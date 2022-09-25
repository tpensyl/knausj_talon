from talon import Module, ctrl, actions, cron
import time
#, multiprocessing, subprocess

mod = Module()

cycle_job=None

cycle_key='up'

global_hold_ms=.128
global_wait_ms=.150

@mod.action_class
class Actions:
    def long_press(key:str, arg_hold_ms:float=None):
        """press"""
        global global_hold_ms
        actions.key(key+':down')
        hold_ms = arg_hold_ms if arg_hold_ms else global_hold_ms
        time.sleep(hold_ms)
        actions.key(key+':up')
    
    def press_wait(key:str, arg_wait_ms:float=None):
        """up"""
        global global_wait_ms
        pause_ms = arg_wait_ms if arg_wait_ms else global_wait_ms
        actions.user.long_press(key)
        time.sleep(pause_ms)

    def cycle_up_down():
        """move up and down continuously"""
        global cycle_key
        actions.key(cycle_key+':up')
        cycle_key= 'down' if cycle_key=='up' else 'up'
        actions.key(cycle_key+':down')

    def start_cycle_up_down(interval:str):
        """Start loop"""
        global cycle_job
        if(cycle_job):
            cron.cancel(cycle_job)
            cycle_job = None
            actions.key('up:up')
            actions.key('down:up')
        else:
            interval_s=1
            cycle_job = cron.interval(interval, actions.user.cycle_up_down)





