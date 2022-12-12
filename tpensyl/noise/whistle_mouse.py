from talon import Module, actions, noise, ctrl


mod = Module()

delta_threshold = 100
speed_scaler = .1

@mod.action_class
class WhistleActions:

    def whistle_start(power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print("whistle start",[int(x) for x in (power, f0, f1, f2)])
        global base1, frame
        base = f1
        frame = 0

    def whistle_stop(power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print("whistle stop",[int(x) for x in (power, f0, f1, f2)])
        global base
        

    def whistle_repeat(power:float, f0:float, f1:float, f2:float): 
        """for debugging"""
        #print("whistle", [int(x) for x in (power, f0, f1, f2)])
        global base
        delta =  f1 - base  
        if abs(delta) > .5:
            print(delta)

            mouse_pos = ctrl.mouse_pos()
            print( mouse_pos )
            ctrl.mouse_move(mouse_pos[0] + delta*speed_scaler, mouse_pos[1])