mode: user.gameboy
win.title: /Railroad Tycoon II.*/
-

help: user.mouse_drag(1)

#<phrase>$: insert(phrase)

settings():
    speech.timeout = .1

speed up: key(+)
slowdown: key(-)
pause: key(pause)

zoom out: key(keypad_2)
zoom in: key(keypad_8)
rotate: key(keypad_4)
rotate back: key(keypad_6)
grid: key(g)

(junk|chuck): key(b)
track: key(t)
train: key(p)
station: key(s)

details: key(d)
overview: key(o)
annual report: key(a)
^newspaper$: key(n)
^last dialogue$: key(ctrl-d)
^find city: key(ctrl-f)

#1-9 changes the tab or specific overview (resources,grades,etc)
#arrow key scroll screen
#ctrl-arrow keys scroll screen faster