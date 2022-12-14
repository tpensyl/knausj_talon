from talon import Module, Context, actions, noise, ctrl

ctx = Context()
ctx.matches = r"""
app.name: disable
"""

mod = Module()

delta_threshold = 100
speed_scaler = .1
pause_threshold = .3
static_base = 650

start_frames = []
ts = 0

@mod.action_class
class WhistleActions:

    def whistle_start(ts:float, power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print("whistle start",[int(x) for x in (10*ts, power, f0, f1, f2)])
        global start_frames, stop_ts
        if ts - stop_ts < pause_threshold:
            print("continue")
            return
        f = f0
        start_frames = [f]

    def whistle_stop(ts:float, power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print("whistle stop",[int(x) for x in (10*ts, power, f0, f1, f2)])
        global stop_ts
        stop_ts = ts 
        

    def whistle_repeat(ts:float, power:float, f0:float, f1:float, f2:float): 
        """for debugging"""
        global start_frames 
        f = f0
        if len(start_frames) < 5:
            start_frames += [f]

        if static_base:
            base = static_base
        else:
            base = sum(start_frames) / len(start_frames)
        
        delta =  f - base  
        if abs(delta) > 0: 
            #print(delta)

            mouse_pos = ctrl.mouse_pos()
            #print( mouse_pos )
            ctrl.mouse_move(mouse_pos[0] + delta*speed_scaler, mouse_pos[1])
        print("whistle", [int(x) for x in [power, f0, f1, f2, f]])