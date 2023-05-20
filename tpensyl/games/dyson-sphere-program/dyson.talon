mode: user.gameboy
app.name: DSPGAME.exe
-
settings():
    user.whistle_scroll_speed = .003
    speech.timeout = 0.1
    key_wait = 30

back: key(esc)
#<phrase>$: skip()

nope: mouse_click(1)
add: user.queue_click()
mode add: user.add_mode()

launch: 
    key(space)
    sleep(100ms)
    key(space)
land: key(alt)
mode jump: user.jump_mode()
#shift: key(shift:down)
scrape: user.fast_fill()
grab: user.click_with_modifier(0, 'shift')
yeet: user.yeet()
mode yeet: user.yeet_mode()
shifty: user.toggle_hold('shift')
drag: user.mouse_drag(0)
change mode: key(r)
litter: 
    key(z)
    user.mouse_drag(0)

tab: key(tab)
copy that: key(,)
paste that: key(.)
up: key(up)
down: key(down)
plus: key(plus)
minus: key(minus)

power: key(2 1 f1)
power tower: key(2 1 f2)
windmill: key(2 1 f4)
miner: key(1 2 f1)
#pump: key(1 2 f3)
oil extractor: key(1 2 f4)
belt: key(1 3 f1)
connect: key(1 3 f4)
splitter: key(1 3 f7)
sprayer: key(1 3 f10)
storage: key(1 4 f1)
smelt: key(1 5 f1)
assemble: key(1 5 f3)
refinery: key(1 5 f6)
chemical [plant]: key(1 5)
research: key(1 7 f1)
foundation: key(1 9 f1)
blueprint: key(0 f1)
force blueprint: key(shift-enter)
build <user.dyson_number_key>: key('f{dyson_number_key}')
upgrade: key(u)

junk: key(x)
craft: key(f)
stuff: key(e)
tech: key(t)
stats: key(p)
mecca: key(c)
journal: key(g)

# tag(): user.whistle_mouse_look