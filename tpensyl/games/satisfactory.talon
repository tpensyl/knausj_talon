mode: user.gameboy
and app.name: Satisfactory
-
#
key(w:down):
    user.set_autorun(true)
key(w:up):
    user.end_long_autorun()
key(a:down): key(left:down)
key(a:up): key(left:up)
key(d:down): key(right:down)
key(d:up): key(right:up)
key(s:down): 
    key(down:down)
    key(up:up)
key(s:up): key(down:up)

(escape | back): key(esc)
power pole: key(1)
power [line]: key(2)
(conveyer | belt): key(3)
gun: key(h)
delete: key(f)
build: key(q)
light: key(b)
crouch: user.toggle_hold('c')
(run|walk): key(shift)
scan:
    key(v:down)
    sleep(2s)
    key(v:up)

fix commands:
    mode.disable("user.gameboy")
    mode.enable("command")
	user.switcher_focus("code")

#<phrase>$: skip()