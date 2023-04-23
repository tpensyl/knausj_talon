mode: user.gameboy
app.name: DSPGAME.exe
-
settings():
    user.whistle_scroll_speed = .003
    speech.timeout = 0.05

back: key(esc)

nope: mouse_click(1)
add: user.queue_click()
add mode: user.add_mode()
shift: key(shift:down)

tab: key(tab)
copy that: key(<)
paste that: key(>)
up: key(up)
down: key(down)
plus: key(plus)
minus: key(minus)

power: key(1 f1)
miner: key(2 f1)
belt: key(3 f1)
connect: key(3 f4)
storage: key(4 f1)
smelt: key(5 f1)
assemble: key(5 f3)
research: key(7 f1)
foundation: key(9 f1)
blueprint: key(0 f1)
build <user.dyson_number_key>: key('f{dyson_number_key}')
upgrade: key(u)

junk: key(x)
craft: key(f)
stuff: key(e)
tech: key(t)
mecca: key(c)
journal: key(g)

# tag(): user.whistle_mouse_look