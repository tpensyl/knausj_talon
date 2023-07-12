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
land: 
    key(alt:down)
    sleep(500ms)
    key(alt:up)
mode jump: user.jump_mode()
#shift: key(shift:down)
scrape: user.fast_fill()
chuck item: key(del)
grab: user.click_with_modifier(0, 'shift')
yeet: user.yeet()
mode yeet: user.yeet_mode()
mode click: user.click_mode() 
mode move: user.move_mode() 
mode jump: user.set_hiss_mode('jump')
mode zoom: user.set_hiss_mode('accelerate')
mode break: user.set_hiss_mode('decelerate')
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
<user.number_string> percent:
    edit.delete_line()
    insert("{number_string}\n")

power: key(2 1 f1)
plugin: 
    user.click_mode()
    key(2 1 f2)
power tower: key(2 1 f2)
[wind] mill: key(2 1 f4)
miner: key(1 2 f1)
water pump: key(1 2 f3)
oil extractor: key(1 2 f4)
belt: key(1 3 f1)
join: key(1 3 f4)
splitter: key(1 3 f7)
sprayer: key(1 3 f10)
storage: key(1 4 f1)
storage tank: key(1 4 f3)
smelt: key(1 5 f1)
assemble: key(1 5 f3)
refinery: key(1 5 f6)
chemical [plant]: key(1 5 f8)
research: key(1 7 f1)
foundation: key(1 9 f1)
blueprint: 
    user.click_mode()
    key(0)
force [blue] print: key(shift-enter)
cut [blue] print: key(ctrl-c) 
build <user.dyson_number_key>: key('f{dyson_number_key}')
upgrade: key(u)

(junk|chuck): key(x)
craft: key(f)
stuff: key(e)
tech: key(t)
stats: key(p)
mecca: key(c)
journal: key(g)

parrot(whistle):
    user.whistle_start(ts, power, f0, f1, f2)
    user.start_camera_drag()

parrot(whistle:repeat):
    user.whistle_repeat(ts, power, f0, f1, f2)

parrot(whistle:stop):
    user.whistle_stop(ts, power, f0, f1, f2)
    user.stop_camera_drag()