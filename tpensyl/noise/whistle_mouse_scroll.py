from talon import Module, Context, actions, ctrl
from math import log, copysign

""" 
    patterns.json
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

mod = Module()
mod.tag("whistle_mouse_scroll", desc="scroll by changing whistle pitch")

ctx = Context()
ctx.matches = """
tag: user.whistle_mouse_scroll
"""


# initialize
ts = 0
stop_ts = 0
start_frames = []

# Add tolerance for accidental 'breaks' during a whistle
pause_threshold = .25

# range is about from A#4-A#5 (466.16-932.33)
# halfway is E5=659.25
min_freq = 466.16
max_freq = 932.33
min_pitch = log(min_freq)
max_pitch = log(max_freq) 
max_speed = 10 
speed_scaler_x = max_speed / (max_pitch - min_pitch)

def shaping_function(pitch_delta):
    "Map difference in pitch into scroll speed"
    x = pitch_delta * speed_scaler_x
    # linear into exponential
    return copysign(abs(x)*(1.5**abs(x)), -x)


@ctx.action_class('user')
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
        f = log(f0)
        if len(start_frames) < 5:
            start_frames += [f]

        base = sum(start_frames) / len(start_frames)
        pitch_delta = f - base
        scroll_speed = shaping_function(pitch_delta)
        
        actions.mouse_scroll(by_lines=False, y=scroll_speed)
        print("whistle", [int(x) for x in [power, f0, f1, f2, f]])
 