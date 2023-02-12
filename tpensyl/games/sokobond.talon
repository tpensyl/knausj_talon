mode: user.gameboy
app.name: Sokobond.exe
-
tag(): user.game_repeater

back: key(esc)
nope:
    key(z)
    sleep(200ms)

(north|up): 
    key(up)
    sleep(200ms)

(south|down): 
    key(down)
    sleep(200ms)

(east|right): 
    key(right)
    sleep(200ms)

(west|left): 
    key(left)
    sleep(200ms)
 