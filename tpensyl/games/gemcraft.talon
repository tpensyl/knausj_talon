
mode: user.gameboy
app.exe: flashplayer_29_gemcraft.exe
-
pause: key(p)
bomb: 
    key(b)
    user.toggle_drag(0)
tower: key(t)
(trench|pit): key(w)
(jam|gem|gym): key(c)
(combine|join): key(g)
join this:
    key(g)
    sleep(10ms)
    user.toggle_drag(0)
join all:
    key(g)
    user.click_with_modifier(0, 'ctrl', 0)
make all:
    key(c)
    user.click_with_modifier(0, 'ctrl', 0)
manna: key(m)
control: user.click_with_modifier(0, 'ctrl')
