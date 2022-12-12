from talon import Module, actions, noise, ctrl


mod = Module()

delta_threshold = 100
speed_scaler = .1

@mod.action_class
class WhistleActions:

    def whistle_start(power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print("whistle start",[int(x) for x in (power, f0, f1, f2)])
        global start_frames
        f = f0
        start_frames = [f]

    def whistle_stop(power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print("whistle stop",[int(x) for x in (power, f0, f1, f2)])
        global base 
        

    def whistle_repeat(power:float, f0:float, f1:float, f2:float): 
        """for debugging"""
        global start_frames
        f = f0
        if len(start_frames) < 5:
            start_frames += [f]

        base = sum(start_frames) / len(start_frames)
        
        delta =  f - base  
        if abs(delta) > 0: 
            #print(delta)

            mouse_pos = ctrl.mouse_pos()
            #print( mouse_pos )
            ctrl.mouse_move(mouse_pos[0] + delta*speed_scaler, mouse_pos[1])
        print("whistle", [int(x) for x in [power, f0, f1, f2, f]+start_frames])