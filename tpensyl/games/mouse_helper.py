from talon import Module, ctrl, actions, cron

mod = Module()

@mod.action_class
class Actions:
    def start_mouse_move_up(speed:float=1):
        "Move mouse up continuously until stopped"
        stop_mouse()
        global move_job
        move_job = cron.interval("10ms", lambda: mouse_move(0, -speed))

    def start_mouse_move_down(speed:float=1):
        "Move mouse down continuously until stopped"
        stop_mouse()
        global move_job
        move_job = cron.interval("10ms", lambda: mouse_move(0, speed))

    def stop_mouse_move():
        "stop automatic mouse movement"
        stop_mouse()

move_job = None

def stop_mouse():
    if move_job:
        cron.cancel(move_job)

def mouse_move(dx, dy):
    import win32api, win32con
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,int(dx),int(dy),0,0)