mode: user.gameboy
and win.title: SteamWorld Quest

-
settings():
    # key_hold = 32
    key_wait = 64
    speech.timeout = 0.1

(stats|inspect): key(e)
(details|deets|sit): key(i)
menu: key(o)
next: key(e)
last: key(q)

(tab|turn): 
    user.release_all_holds()
    key(tab)
turn force: key(tab up enter)

an turn: key(tab)
(back|bacca): key(esc)

run: user.toggle_hold('shift')

short <user.arrow_key>: user.long_press(arrow_key, .5)
step <user.arrow_key>: user.long_press(arrow_key, 1)
go <user.arrow_key>: user.long_press(arrow_key, 2)

page down: key(pagedown)
page up: key(pageup)

<user.arrow_key>: key(arrow_key)
<user.arrow_key> <number_small>: key('{arrow_key}:{number_small}')
(yeah|slap): key(enter)

^<number_small>$:
    key('right:{number_small}')
    key(space)

use <number_small>:
    key('right:{number_small}')
    key(space:2)
    
(discard|chuck): user.long_press('r', 2)

(discard|chuck) <number_small>:
    key('right:{number_small}')
    user.long_press('r', 2)