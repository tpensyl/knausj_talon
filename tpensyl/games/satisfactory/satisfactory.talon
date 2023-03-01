mode: user.gameboy
and app.name: Satisfactory
-
tag(): user.whistle_mouse_scroll

settings():
    speech.timeout = 0.2

pogo: user.set_tertiary_noise_action("jump")
drag mode: user.set_tertiary_noise_action("drag")
lunge mode: user.set_tertiary_noise_action("lunge")
use: 
    user.long_press('i')
    user.set_tertiary_noise_action("use")
get: 
    #user.set_hold('up')
    user.set_hold('up', false)
    user.long_press('i')
    sleep(5ms)
(back|escape):
    user.mouse_drag_end()
    user.satisfactory_back()
    sleep(10ms)

^photo mode$: key(p)
^screenshot$: key(f12)

^drag$: user.mouse_drag(0)
^end drag | drag end$: user.mouse_drag_end()
^drop|poop$: user.satisfactory_drop()

# key(w:down):        user.hold_on_double_press_down('up')
# key(ctrl-w:down):   user.hold_on_double_press_down('up')
# key(w:up):          user.hold_on_double_press_up('up')
# key(ctrl-w:up):     user.hold_on_double_press_up('up')
# key(a:down):        key(left:down)
# key(ctrl-a:down):   key(left:down)
# key(a:up):          key(left:up)
# key(ctrl-a:up):     key(left:up)
# key(d:down):        key(right:down)
# key(ctrl-d:down):   key(right:down)
# key(d:up):          key(right:up)
# key(ctrl-d:up):     key(right:up)
# key(s:down):        user.hold_on_double_press_down('down')
# key(ctrl-s:down):   user.hold_on_double_press_down('down')
# key(s:up):          user.hold_on_double_press_up('down')
# key(ctrl-s:up):     user.hold_on_double_press_up('down')


# key(e:down): user.hold_on_double_press_down('i')
# key(e:up): user.hold_on_double_press_up('i')

build$: key(q)
build <user.number_key>: key(number_key)
pick <user.number_key>: 
    #user.release_all_holds()
    key(number_key)
    sleep(15ms)
    user.set_hold('i', true)
^change mode$: key(r)
^pick mode$: user.long_press('r', 2.3)
^reload$: key(r)
^rebuild$: key(q:2)
belt$: key(1)
pick belt:
    key(1)
    sleep(15ms)
    user.set_hold('i', true)
power$: key(2)
(lift|left|liff)$: key(3)
^(belt pole|pipe)$: key(4)

^(bar|tab) next:
    user.scroll_with_modifier('alt', 1, '18ms')
^(bar|tab) next <user.repeat_num>:
    user.scroll_with_modifier('alt', 1, '18ms', repeat_num)
^(bar|tab) last:
    user.scroll_with_modifier('alt', -1, '18ms')
^(bar|tab) last <user.repeat_num>:
    user.scroll_with_modifier('alt', -1, '18ms', repeat_num)

^(recipe|recipes)$: key('o')
^gun$: key(h)
junk$: key(f)
^(stuff|item)$: key(tab)
^flashlight$: key(b)
paint$: key(x)

^mid click$: mouse_click(2)
^split$: mouse_click(1)
^long split$: user.long_click(1, 300000)
^boom$: mouse_click(1)
^gather$: user.toggle_hold('i')
^control$: user.toggle_hold('ctrl')
^split power$: 
    key(shift:down)
    mouse_click(0)
    key(shift:up)
    # untoggle run
    key(shift)
crouch$: user.toggle_hold('c')
^stand$: user.set_hold('c', false)
^toggle ping$: user.toggle_hold('alt')
^(backpedal)$:
    user.set_hold('down', true)
^(sprint|walk): key(shift)

^look upper: 
    user.set_toggle_mouse_speed(50)
    user.set_hold('mouse_move_up', true)
^look downer: 
    user.set_toggle_mouse_speed(50)
    user.set_hold('mouse_move_down', true)
^look stop: user.stop_mouse_move()

^lefty$: 
    user.set_hold('left', true, true)
    sleep(1s)
    user.set_hold('left', false)
^righty$: 
    user.set_hold('right', true, true)
    sleep(1s)
    user.set_hold('right', false)
^slight left$: 
    user.set_hold('left', true, false)
    sleep(500ms)
    user.set_hold('left', false)
^slight right$: 
    user.set_hold('right', true, false)
    sleep(500ms)
    user.set_hold('right', false)
^(letter queue|truck record)$: key(q)
^(letter f | truck load)$: user.toggle_hold('f')
^(letter ex)$: key(x)
^(letter ah | hide hud)$: key(h)


^jump$: user.long_press('space')
^lunge$: user.satisfactory_lunge()
# e.g. from underwater
^surface$: user.long_press('space', 2)
^scan$: 
    user.long_press('v', 2.3)
    user.block_scan(46)
    user.start_stopwatch()
^compass show$: user.block_compass(0)
^compass hide$: user.block_compass(-1)

^press <user.keys>: key(keys)
^say <user.prose>: insert(prose)
^enter$: key(enter)
^chat <user.prose>:
    key(enter)
    sleep(10ms)
    insert(prose)
    key(enter)
^emote$:
    user.long_press('t', 3.3)
copy that: key(ctrl-c)
paste that: key(ctrl-v)
<user.number_string> percent:
    edit.delete_line()
    insert("{number_string}\n")
<user.number_string> (point|dot) <number_small> percent:
    edit.delete_line()
    insert("{number_string}.{number_small}\n")
    

#^<phrase>$: skip()