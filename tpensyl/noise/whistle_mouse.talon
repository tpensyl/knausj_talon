tag: user.whistle_mouse
-

parrot(whistle):
    #user.sound_debug("twhistle", power, f0, f1, f2)
    user.whistle_start(ts, power, f0, f1, f2)

parrot(whistle:repeat):
    #user.sound_debug("twhistle start", power, f0, f1, f2)
    user.whistle_repeat(ts, power, f0, f1, f2)

parrot(whistle:stop):
    #user.sound_debug("twhistle start", power, f0, f1, f2)
    user.whistle_stop(ts, power, f0, f1, f2)