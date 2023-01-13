mode: user.gameboy
and app.name: Satisfactory
-
tag(): user.game_media
tag(): user.whistle_mouse_scroll
pogo: user.set_tertiary_noise_action("jump")
use: 
    user.long_press('e')
    user.set_tertiary_noise_action("use")

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

^build <user.number_key>$: key(number_key)
^belt$: key(1)
^power$: key(2)
^belt pole$: key(4)
^lift$: key(6)
^tower$: key(0)
^(bar|tab) next$: user.scroll_with_modifier('alt', 1, '10ms')
^(bar|tab) last$: user.scroll_with_modifier('alt', -1, '10ms')

^(recipe|recipes)$: key('o')
^back$: key(esc)
^gun$: key(h)
^delete$: key(f)
^build$: key(q)
^(stuff|item)$: key(tab)
^light$: key(b)
^paint$: key(x)

^forage$: key(i:down)
^control$: user.toggle_hold('ctrl')
^crouch$: user.toggle_hold('c')
^backpedal$: user.toggle_hold('s')
^(run|walk)$: key(shift)
^jump$: user.long_press('space')
^scan$:
    key(v:down)
    sleep(2s)
    key(v:up)
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

#<phrase>$: skip()