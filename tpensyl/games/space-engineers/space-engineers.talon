mode: user.gameboy
and app.name: Space Engineers
-
tag(): user.whistle_mouse_scroll

settings():
    speech.timeout = 0.1
    key_wait = 10
    key_hold = 30

use: key(f)
stuff: key(k)
helmet: key(j)
crouch: key(c)
jetpack: key(x)
flashlight: key(l)
configure: key(g)
park: key(p)

third person: key(v)
inertia: key(z)

destroy: user.start_destroying()

please respond: key(backspace)
test: mouse_click(2, 32000)

grab: 
    mouse_click(0, hold=32000)
    sleep("20ms")
    mouse_click(0, hold=32000)
make ten: user.click_with_modifier(0, 'ctrl', "100ms")
make thirty: 
    user.click_with_modifier(0, 'ctrl', "100ms")
    user.click_with_modifier(0, 'ctrl', "100ms")
    user.click_with_modifier(0, 'ctrl', "100ms")
make [a|one] hundred: user.click_with_modifier(0, 'shift', "100ms")
make [a|one] thousand: user.click_with_modifier(0, 'ctrl-shift', "100ms")

rotate left: key(delete)
rotate right: key(pagedown)
rotate up: key(home)
rotate down: key(end)

pogo: user.set_tertiary_noise_action("jump")
jetpack mode: user.set_tertiary_noise_action("jetpack")

drag mode: user.set_tertiary_noise_action("drag")
lunge mode: user.set_tertiary_noise_action("lunge")
(back|escape):
    user.mouse_drag_end()
    user.satisfactory_back()
    sleep(10ms)


^drag$: user.mouse_drag(0)
^end drag | drag end$: user.mouse_drag_end()
^drop|poop$: user.satisfactory_drop()

###

holster: key(0)
(welder|welter): key(ctrl-1 1)
grind: key(ctrl-1  2)
drill: key(ctrl-1  3)
pipe: key(ctrl-1  4)

tab <number>: key("ctrl-{number}")
(build|make) <user.satisfactory_number_key>: key(satisfactory_number_key)
###


^split$: mouse_click(1)
^long split$: user.long_click(1, 300000)
^(boom|boon)$: mouse_click(1)
^gather$: user.toggle_hold('i')
# remapped the control key to a non modifier, to simplify key intercept
^control$: user.toggle_hold('z')
^split power$: 
    key(shift:down)
    mouse_click(0)
    key(shift:up)
    # untoggle run
    key(shift)
^toggle ping$: user.toggle_hold('alt')
backpedal:
    user.set_hold('s', true)
^(sprint|walk): key(shift)

^lefty$: 
    user.set_hold('left', true, true)
    sleep(1s)
    user.set_hold('left', false)
^righty$: 
    user.set_hold('right', true, true)
    sleep(1s)
    user.set_hold('right', false)
slight left: 
    user.set_hold('left', true, false)
    sleep(500ms)
    user.set_hold('left', false)
slight right: 
    user.set_hold('right', true, false)
    sleep(500ms)
    user.set_hold('right', false)

# Left Peddle (strafe)
# key(f16:down): user.set_hold('left', true)
# key(f16:up): user.set_hold('left', false)

# Left Peddle
key(f16:down): user.set_hold('mouse_move_left', true)
key(f16:up): user.set_hold('mouse_move_left', false)

# Right Peddle (strafe)
# key(f18:down): user.set_hold('right', true)
# key(f18:up) user.set_hold('right', false)

# # Right Peddle
# key(f18:down): user.set_hold('mouse_move_right', true)
# key(f18:up): user.set_hold('mouse_move_right', false)

# Right Peddle
key(f18:down): key(space:down)
key(f18:up): key(space:up)

# Bottom Peddle
key(f17:down): user.set_hold('mouse_move_up', true)
key(f17:up): user.set_hold('mouse_move_up', false)

# Top Peddle
key(f19:down): user.set_hold('mouse_move_down', true)
key(f19:up): user.set_hold('mouse_move_down', false)

#^jump$: user.long_press('space')
^(lunge|lunch)$: user.satisfactory_lunge()
# e.g. from underwater

^press <user.keys>: key(keys)
^say <user.prose>: insert(prose)
^enter$: key(enter)
# ^chat <user.prose>:
#     key(enter)
#     sleep(10ms)
#     insert(prose)
#     key(enter)
copy that: key(ctrl-c)
paste that: key(ctrl-v)
<user.number_string> percent:
    edit.delete_line()
    insert("{number_string}\n")
    # a click is required to return focus to the game
    user.satisfactory_click()
<user.number_string> (point|dot) <number_small> percent:
    edit.delete_line()
    insert("{number_string}.{number_small}\n")
    user.satisfactory_click()
    

<phrase>$: skip()