mode: user.gameboy
and win.title: SteamWorld Quest

-
settings():
    # key_hold = 32
    key_wait = 64
    speech.timeout = 0.1

stats: key(e)
menu: key(o)
next: key(e)
last: key(q)

tab: 
    user.release_all_holds()
    key(tab)

an turn: key(tab)
back: key(esc)

run: user.toggle_hold('shift')

go right: user.long_press('right', 2)
go left: user.long_press('left', 2)
go (north|up): user.long_press('up', 1)
go (south|down): user.long_press('down', 1)

left: key(left)
right: key(right)
(yeah|slap): key(enter)

<number_small>:
    key('right:{number_small}')
    key(space)

use <number_small>:
    key('right:{number_small}')
    key(space:2)
    
(discard|chuck): user.long_press('r', 2)

(discard|chuck) <number_small>:
    key('right:{number_small}')
    user.long_press('r', 2)