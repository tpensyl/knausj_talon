from talon import Module, ctrl, actions, cron
import math

mod = Module()

@mod.action_class
class Actions:
    def start_mouse_move_up(speed:int=100):
        "Move mouse up continuously until stopped"
        start_vertical_motion(-speed)

    def start_mouse_move_down(speed:int=100):
        "Move mouse down continuously until stopped"
        start_vertical_motion(speed)

    def stop_mouse_move():
        "stop automatic mouse movement"
        stop_mouse()

move_job = None

def start_vertical_motion(velocity:int):
    stop_mouse()
    speed = abs(velocity)
    dir = math.copysign(1, velocity) 
    interval = int(1000 / abs(velocity))
    interval_str = str(interval) + "ms"
    global move_job
    move_job = cron.interval(interval_str, lambda: mouse_move(0, dir))


def stop_mouse():
    if move_job:
        cron.cancel(move_job)

def mouse_move(dx, dy):
    import win32api, win32con
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,int(dx),int(dy),0,0)