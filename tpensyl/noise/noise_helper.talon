#app.title: disable
-
tag(): user.whistle_mouse

parrot(palate_click):
    user.sound_debug("palate", power, f0, f1, f2)
    user.parrot_palate()

parrot(tut):
    user.sound_debug("tut", power, f0, f1, f2)
    user.parrot_tut()