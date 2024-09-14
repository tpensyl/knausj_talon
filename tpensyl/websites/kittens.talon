win.title: /Kittens Game -.*/
-
settings():
    speech.timeout = 0.2
touch <number>: user.game_click(0, number, "2ms")

key(ctrl-shift-space): user.mouse_auto_click(100)
^auto click fast$: user.mouse_auto_click(4000)
^auto click$: user.mouse_auto_click(10000)
^auto click long$: user.mouse_auto_click(40000)
key(space): user.mouse_auto_click(10000) 
key(ctrl-space): user.mouse_auto_click(40000) 
key(shift-space): user.mouse_auto_click(1000)

# Requires rango
autoclick long <user.rango_hint>: user.rango_auto_click(rango_hint, 40000)
autoclick slow <user.rango_hint>: user.rango_auto_click(rango_hint, 10000)
autoclick <user.rango_hint>$: user.rango_auto_click(rango_hint, 5000)
autoclick fast <user.rango_hint>: user.rango_auto_click(rango_hint, 1000)

(build|bonfire): key(1)
^(village|settlement|town|city|metro|mega|empire|dominion|hegemony)$: key(2)
science: key(3)
workshop: key(4)
trade: key(5)
religion: key(6)
[outer] space: key(7)
^time: key(8)
^challenge: key(9)