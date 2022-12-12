-

parrot(palate_click):
    user.sound_debug("tut", power, f0, f1, f2)
    user.parrot_palate()

parrot(tut):
    user.sound_debug("tut", power, f0, f1, f2)
    user.parrot_tut()

parrot(whistle):
    #user.sound_debug("twhistle", power, f0, f1, f2)
    user.whistle_start(power, f0, f1, f2)

parrot(whistle:repeat):
    #user.sound_debug("twhistle start", power, f0, f1, f2)
    user.whistle_repeat(power, f0, f1, f2)

parrot(whistle:stop):
    #user.sound_debug("twhistle start", power, f0, f1, f2)
    user.whistle_stop(power, f0, f1, f2)