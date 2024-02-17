mode: user.gameboy
app.name: Sokobond.exe
-
tag(): user.game_repeater

(enter | slap): key(enter)
(escape | menu): key(esc)
(reset|restart) (level|puzzle): key(r)
(nope | back):
    key(z)
    sleep(220ms)

(north|up): 
    key(up)
    sleep(220ms)

(south|down): 
    key(down)
    sleep(220ms)

(east|right): 
    key(right)
    sleep(220ms)

(west|left): 
    key(left)
    sleep(220ms)
 