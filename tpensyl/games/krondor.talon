#mode: user.gameboy
#win.title: /DOSBox.*KRONDOR*/
-
settings():
    # minimum silence time (in seconds) before speech is cut off, default 0.3
    speech.timeout = .2
    user.default_long_press_ms = .032
    user.default_long_wait_ms = .05
    #user.mouse_wait = 50000
    #user.mouse_hold = 50000

turn left: 
    user.multi_press('left', 8)

try it: user.mouse_drag_end() 
#pull <phrase>$: "pull {phrase}"
<user.letter>: key(letter)