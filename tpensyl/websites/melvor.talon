win.title: /^Melvor Idle.*/
win.title: /Hitpoints .*/
-
settings():
    speech.timeout = 0.18
    key_hold = 100
    # for map hotkeys

touch <number>: user.game_click(0, number, "2ms")

^auto click fast$: user.mouse_auto_click(4000)
^auto click$: user.mouse_auto_click(10000)
^auto click long$: user.mouse_auto_click(40000)

# Requires rango
autoclick <user.rango_hint>: user.rango_auto_click(rango_hint, 10000)
autoclick long <user.rango_hint>: user.rango_auto_click(rango_hint, 40000)

# key(space): user.mouse_auto_click(10000) 
key(ctrl-space): user.mouse_auto_click(10000)