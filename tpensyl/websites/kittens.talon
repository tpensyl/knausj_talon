win.title: /Kittens Game - Y.*/
win.title: /Kittens Game - a .*/
-
settings():
    speech.timeout = 0.18
touch <number>: user.kitten_click(number)
touch ten:
    key(ctrl:down)
    user.game_click(0)
    key(ctrl:up)

build all:
    key(shift:down)
    mouse_click(0)
    key(shift:up)
    sleep(250ms)
    key(enter)

kitten test:
    user.kitten_test()

start loop: user.kitten_end_game_loop()
finish loop: user.kitten_end_game_loop_b()

key(ctrl-alt-space): 
    sleep(400ms)
    user.mouse_auto_click(350)
^auto click ultra fast$: user.mouse_auto_click(350)
^auto click very fast$: user.mouse_auto_click(1000)
^auto click fast$: user.mouse_auto_click(4000)
^auto click$: user.mouse_auto_click(10000)
^auto click long$: user.mouse_auto_click(40000)
key(space): user.mouse_auto_click(10000) 
key(ctrl-space): user.mouse_auto_click(4000) 
# key(ctrl-alt-space): user.mouse_auto_click(500)

# Requires rango
autoclick long <user.rango_target>$: user.rango_auto_click(rango_target, 40000)
autoclick slow <user.rango_target>$: user.rango_auto_click(rango_target, 10000)
autoclick <user.rango_target>$: user.rango_auto_click(rango_target, 5000)
autoclick fast <user.rango_target>$: user.rango_auto_click(rango_target, 1000)
button autoclick <user.text>$: user.rango_auto_click_string(text, 5000)

touch leviathan: 
    mouse_click(0)
    user.rango_run_action_on_text_matched_element("clickElement", "leviathan", false)
    mouse_click(0)
    user.rango_run_action_on_text_matched_element("clickElement", "leviathan", false)
    mouse_click(0)
    user.rango_run_action_on_text_matched_element("clickElement", "leviathan", false)
    mouse_click(0)
    user.rango_run_action_on_text_matched_element("clickElement", "leviathan", false)
    mouse_click(0)
    user.rango_run_action_on_text_matched_element("clickElement", "leviathan", false)
    mouse_click(0)
    user.rango_run_action_on_text_matched_element("clickElement", "leviathan", false)
    mouse_click(0)
    user.rango_run_action_on_text_matched_element("clickElement", "leviathan", false)
    mouse_click(0)
    user.rango_run_action_on_text_matched_element("clickElement", "leviathan", false)
    mouse_click(0)
    user.rango_run_action_on_text_matched_element("clickElement", "leviathan", false)
    mouse_click(0)
    user.rango_run_action_on_text_matched_element("clickElement", "leviathan", false)

^(build|bonfire|one four): key(1)
^(village|settlement|town|city|metro|mega|empire|amper|dominion|hegemony|federation|rike|society|civilization|consortium)$: key(2)
^science: key(3)
^workshop: key(4)
^trade: key(5)
^religion: key(6)
^[outer] space: key(7)
^(time|ten): key(8)
^challenge: key(9)
