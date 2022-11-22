mode: user.gameboy
and win.title: /.*AKLABETH.*/
-

(up|north): user.press_wait('up')
(down|back|south): user.press_wait('down')
(left|west): user.press_wait('left')
(right|east): user.press_wait('right')
(enter|climb): user.press_wait('e')
climb up:
    'am'
    sleep(.5)
    '1'
    sleep(.5)
    user.press_wait('e')
climb down:
    'am'
    sleep(.5)
    '2'
    sleep(.5)
    user.press_wait('e')
(swing [axe]|chop|stab): 
    "aas"
    sleep(1)
#stab: "ar"
punch: "af"
status: key('z')
full screen: key(f11+f)
buy food: key('f')
buy axe: key('a')
buy rapier: 'r'
buy shield: 's'
buy (magic|amulet): 'm'
quit: 'q'
wait: key( space )
magic: 'am'
choose <number_small>: key('{number_small}')
escape: key(esc)

settings():
    user.default_long_press_ms = .001
    user.default_long_wait_ms = .3
    speech.timeout = 0.1