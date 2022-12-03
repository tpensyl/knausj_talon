mode: user.gameboy
app.name: Age of Empires: Definitive Edition
-

pause: key(f3)

town: key(h)
(vill|villager): key(q)

idle: key(.) 
queue: 
	key("shift:down")
	mouse_click(1)
	key("shift:up")
add:
    key("ctrl:down")
	mouse_click(0)
	key("ctrl:up")

repair: key(n)

go: key(a)
stop: key(e)

delete units: key(del)

set <number_small>: key('ctrl-{number_small}')
<number_small>: key('{number_small}')

zoom men: key(ctrl-plus)
zoom way in: key(shift-numpad_+)
zoom out: key(ctrl-minus)
zoom way out: key(shift-numpad_minus)


#build: key(q)
house: key(q)
granary: key(e)
dock: key(t)
barracks: key(w)
market: key(d)
stonewall: key(u)
tower: key(y)
farm: key(f)
archery range: key(a)
stable: key(s)
temple: key(h)
town center: key(j)
siege workshop: key(z)
government center: key(g)
wonder: key(c)
storage [pit]: key(r)
academy: key(x)

fish boat: key(q)

bowman: key(q)

#<phrase>: skip()

<number_small> times: core.repeat_command(number_small-1)
<user.ordinals>: core.repeat_command(ordinals-1)
