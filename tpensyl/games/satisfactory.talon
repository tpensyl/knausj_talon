mode: user.gameboy
and app.name: Satisfactory
-
tag(): user.game_media
tag(): user.whistle_mouse_scroll
pogo: user.set_tertiary_noise_action("jump")
use: 
    user.long_press('e')
    user.set_tertiary_noise_action("use")
get: user.long_press('e')

key(w:down):        user.hold_on_double_press_down('up')
key(ctrl-w:down):   user.hold_on_double_press_down('up')
key(w:up):          user.hold_on_double_press_up('up')
key(ctrl-w:up):     user.hold_on_double_press_up('up')
key(a:down):        key(left:down)
key(ctrl-a:down):   key(left:down)
key(a:up):          key(left:up)
key(ctrl-a:up):     key(left:up)
key(d:down):        key(right:down)
key(ctrl-d:down):   key(right:down)
key(d:up):          key(right:up)
key(ctrl-d:up):     key(right:up)
key(s:down):        user.hold_on_double_press_down('down')
key(ctrl-s:down):   user.hold_on_double_press_down('down')
key(s:up):          user.hold_on_double_press_up('down')
key(ctrl-s:up):     user.hold_on_double_press_up('down')


key(e:down): user.hold_on_double_press_down('i')
key(e:up): user.hold_on_double_press_up('i')

build$: key(q)
build <user.number_key>$: key(number_key)
^change mode$: key(r)
^rebuild$: key(q:2)
belt$: key(1)
power$: key(2)
^belt pole$: key(4)
lift$: key(6)

^(bar|tab) next [one]$:
    user.scroll_with_modifier('alt', 1, '10ms')
^(bar|tab) next <user.repeat_num>$:
    user.scroll_with_modifier('alt', 1, '10ms', repeat_num)
^(bar|tab) last$:
    user.scroll_with_modifier('alt', -1, '10ms')
^(bar|tab) last <user.repeat_num>$:
    user.scroll_with_modifier('alt', -1, '10ms', repeat_num)

^(back|escape):
    user.mouse_drag_end()
    user.satisfactory_back()
^(recipe|recipes)$: key('o')
^gun$: key(h)
^(doze|junk)$: key(f)
^(stuff|item)$: key(tab)
^flashlight$: key(b)
paint$: key(x)

^mid click$: mouse_click(2)
^split$: mouse_click(1)
^gather$: key(i:down)
^control$: user.toggle_hold('ctrl')
^hold shift$: user.toggle_hold('shift')
crouch$: user.toggle_hold('c')
^stand$: user.set_hold('c', false)
^toggle ping$: user.toggle_hold('alt')
^(backpedal)$:
    #user.set_hold('c', true)
    #sleep(5ms)
    user.set_hold('down', true)
^(run|walk): key(shift)
^jump$: user.long_press('space')
^surface$: user.long_press('space', 1)
^scan$: 
    user.long_press('v', 2)
    user.block_compass()
^drag$:
    user.mouse_drag(0)
^end drag | drag end$: user.mouse_drag_end()

^fix commands$:
    mode.disable("user.gameboy")
    mode.enable("command")
	user.switcher_focus("code")

^alt tab$:
    user.window_tab()
    mode.disable("user.gameboy")
    mode.enable("command")
    user.switcher_focus("code")

#^<phrase>$: skip()