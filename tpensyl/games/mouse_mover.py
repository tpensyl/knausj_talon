from talon import Module, ctrl, actions, cron
import math

mod = Module()

@mod.action_class
class Actions:
    def mouse_move_smooth(target_x:int, target_y:int, interval_ms:int, total_ms:int):
        "move mouse to target position in a series of small steps"
        start = ctrl.mouse_pos()
        t = 0
        while t < 1:
            x, y = interpolate(start, (target_x, target_y), t)
            print(x, y)
            ctrl.mouse_move(x, y)
            actions.sleep(str(interval_ms) + "ms")
            t += interval_ms / total_ms

    def start_mouse_move_right(speed:int=100):
        "Move mouse right continuously until stopped"
        start_mouse_motion(speed, False)

    def start_mouse_move_down(speed:int=100):
        "Move mouse down continuously until stopped"
        start_mouse_motion(speed, True)

    def stop_mouse_move():
        "stop automatic mouse movement"
        stop_mouse()

    def mouse_auto_click(interval_ms:int=2000):
        "autoclick until mouse moves"
        mouse_initial_pos = ctrl.mouse_pos()
        cron_interval = str(interval_ms) + "ms"
        mouse_click_repeat(mouse_initial_pos, cron_interval)
              

def mouse_click_repeat(mouse_initial_pos, interval):
        if(ctrl.mouse_pos() == mouse_initial_pos):
            ctrl.mouse_click(0)
            cron.after(interval, lambda: mouse_click_repeat(mouse_initial_pos, interval)) 

def interpolate(xy1, xy2, t):
    x1, y1 = xy1
    x2, y2 = xy2
    return x1 + (x2 - x1) * t, y1 + (y2 - y1) * t

move_job = None
def start_mouse_motion(velocity:int, vertical=True):
    stop_mouse()
    speed = abs(velocity)
    dir = math.copysign(1, velocity) 
    interval = int(1000 / abs(velocity))
    interval_str = str(interval) + "ms"
    global move_job
    vector = (0, dir) if vertical else (dir, 0)
    move_job = cron.interval(interval_str, lambda: mouse_move(*vector))


def stop_mouse():
    if move_job:
        cron.cancel(move_job)

def mouse_move(dx, dy):
    import win32api, win32con
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,int(dx),int(dy),0,0)