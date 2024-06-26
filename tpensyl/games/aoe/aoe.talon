mode: user.gameboy
app.name: Age of Empires: Definitive Edition
-

# # <phrase>: skip() 
# cheat reveal map:
# 	key(enter)
# 	sleep(20ms)
# 	insert("REVEAL MAP")
# 	sleep(20ms)
# 	key(enter)

# cheat no fog:
# 	key(enter)
# 	sleep(20ms)
# 	insert("NO FOG")
# 	sleep(20ms)
# 	key(enter)

cheat medusa:
	key(enter)
	sleep(20ms)
	insert("MEDUSA")
	sleep(20ms)
	key(enter)

settings():
    # minimum silence time (in seconds) before speech is cut off, default 0.3
    speech.timeout = 0.15
	#key_wait = 30

back:
	key(esc)
	
drag: 
	user.mouse_drag(0) 
screen drag: 
	user.mouse_drag(1) 

pause: key(f3)
speedup: key(keypad_plus) 
slowdown: key(keypad_minus) 
slow way down: key(keypad_minus:2)
clock: key(f11)

##### Cheat Engine Hotkeys
# speed zero: key(f14)
# speed one: key(f20)
# speed too: key(f21)
# speed three: key(f22)
# speed for: key(f23)


zoom men: 
	sleep(50ms)
	key(ctrl-keypad_plus)
zoom way in: key(shift-keypad_plus)
zoom out: 
	sleep(50ms)
	key(ctrl-keypad_minus)
zoom way out: key(shift-keypad_minus)

# Jump camera/focus
go town [center]: key(ctrl-shift-h)
go market: key(ctrl-shift-m)
go (barracks|borax): key(ctrl-shift-b)
go (archer|archery) [range]: key(ctrl-shift-a)
go stable: key(ctrl-shift-l)
go siege [workshop]: key(ctrl-shift-k)
go dock: key(ctrl-shift-d)
go temple: key(ctrl-shift-p)
go academy: key(ctrl-shift-y)
go granary: key(ctrl-shift-g)
go storage [pit]: key(ctrl-shift-s)
go government [center]: key(ctrl-shift-c)
go wonder: key(ctrl-o)
go battle: key(backspace)

tech tree: key(f6)
diplomacy: key(f7)
objectives: key(f9)
menu$: key(f10)

idle [ville|villager]: key(.)
idle military: key(,)
all idle: key(ctrl-shift-.) 

(queue|cute): 
	key("shift:down")
	mouse_click(0)
	key("shift:up")
^(add|had)$:
    key("ctrl:down")
	mouse_click(0)
	key("ctrl:up")
(add all):
    key("ctrl:down")
	mouse_click(0)
	mouse_click(0)
	key("ctrl:up")

merge {user.control_group}:
	key('shift-{control_group}')
	key('ctrl-{control_group}')
group {user.control_group}: key('ctrl-{control_group}')
^{user.control_group}$: key('{control_group}')
go {user.control_group}: key('alt-{control_group}')
take {user.control_group}: key('shift-{control_group}')

delete unit: 
	key(del)
	sleep(10ms)

# Military
(attack [move] | stab): 
	key(a)
	mouse_click(0)

(stand ground | hold): key(e)
aggressive: key(q)
defensive: key(w)
no attack: key(r)
attack ground: key(s)

# Transport
unload: key(q) 

# Training general
<user.repeat_num> times: core.repeat_command(repeat_num-1) 
many times: core.repeat_command(50)
#<user.ordinals>: core.repeat_command(ordinals-1)
twice: 
	sleep(10ms)
	core.repeat_command(1)
	
stop: key(m)

# Towns Center
(vil|villager|ville): key(q)
(town bill | townville):
	key(ctrl-shift-h)
	sleep(10ms)
	key(q)

# Villager
[build] house: key(q)
build granary: key(e)
build dock: key(t)
build barracks: key(w)
build market: key(d)
[build] [stone] wall: key(u)
[build] [watch] tower: key(y)
build farm: key(f)
build (archery | archer) range: key(a)
build stable: key(s)
build temple: key(h)
build town [center]: key(j)
build siege [workshop]: key(z)
build government [center]: key(g)
build wonder: key(c)
build storage [pit]: key(r)
build academy: key(x)
repair: key(n)

# Dock
(fish|fishing) [boat|ship]: key(q)
transport [boat|ship]: key(e)
(trade|merchant) [boat|ship]: key(w)
(scout [ship] | [war] galley | trireme): key(r)
(catapult [trireme] | juggernaut): key(t)
fire (galley | ship | boat): key(y)

# Barracks
(club man | ax man): key(q)
(swordsman | legion): key(w)
slinger: key(e)

# Archery Range
bowman: key(q)
(improved|composite) bowman | composite: key(w)
elephant archer: key(t)
horse archer: key(r)
chariot archer: key(e)

# Stable
scout: key(q)
(calvary | cataphract): key(e)
chariot: key(w)
(war elephant | armored elephant): key(r)
camel [rider]: key(t)

# Siege Workshop
(stone thrower | catapult): key(q)
(ballista | helepolis): key(w)

# Temple
priest: key(q)

# Academy
(hoplite | phalanx | centurion): key(q)



