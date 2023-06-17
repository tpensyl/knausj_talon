mode: user.gameboy
and win.title: /.*BStone.*/
-
tag(): user.game_generic_keys

settings():
    key_hold = 32
    key_wait = 16
    speech.timeout = 0.1

test: key(up)
(get|open): key(space)