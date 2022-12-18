from talon import Module, Context, actions, ctrl
from math import log, copysign

""" patterns.json
	"whistle": {
		"sounds": ["sound_whistle"],
		"threshold": {
			">power": 20,
			">probability": 0.85,
			">f0": 250
		},
		"graceperiod": 0.1,
		"grace_threshold": {
			">power": 10,
			">probability": 0.3,
			">f0": 250
		}
	},
"""

ctx = Context()
ctxtags = ["user.whistle_mouse_scroll"]

mod = Module()
mod.tag("whistle_mouse_scroll", desc="scroll by changing whistle pitch")

# initialize
ts = 0
stop_ts = 0

# relative scaling, based on first sound
start_frames = []
delta_threshold = 100
pause_threshold = .2

# range is about from A#4-A#5 (466.16-932.33)
# halfway is E5=659.25
minimum_freq = 466.16
maximum_freq = 932.33
minimum_log = log(minimum_freq)
maximum_log = log(maximum_freq) 

max_speed = 10 
speed_scaler_x = max_speed / (maximum_log - minimum_log)

@ctx.action_class('self')
class WhistleActions:

    def whistle_start(ts:float, power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print("whistle start",[int(x) for x in (10*ts, power, f0, f1, f2)])
        global start_frames, stop_ts
        if ts - stop_ts < pause_threshold:
            print("continue")
            return 
        
        f = log(f0)
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
            start_frames += [log(f)]

        base = sum(start_frames) / len(start_frames)
        
        delta = -(log(f) - base) * speed_scaler_x
        # linear into exponential
        delta =copysign(abs(delta)*(1.5**abs(delta)), delta)
        
        #actions.user.swoop_move(delta)
        actions.mouse_scroll(by_lines=False, y=int(delta))
        print("whistle", [int(x) for x in [power, f0, f1, f2, f]])

    # def swoop_move(delta:float):
    #     mouse_move(delta)
 