tag: user.whistle_mouse_look
-

parrot(whistle):
    user.whistle_start(ts, power, f0, f1, f2)

parrot(whistle:repeat):
    user.whistle_repeat(ts, power, f0, f1, f2)

parrot(whistle:stop):
    user.whistle_stop(ts, power, f0, f1, f2)

parrot(yee):
    print("ye")
    user.whistle_start(ts, power, f0, f1, f2)