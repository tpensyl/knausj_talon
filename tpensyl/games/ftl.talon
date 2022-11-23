mode: user.gameboy
win.title: /FTL: Faster Than Light/
app.exe: FTLGame.exe
-

<phrase>: skip()
^jump$: key(j)
^ship$: key(u)
^(closed|clothes|close) doors$: key(x)
^return$: key(enter)
^drag$: user.mouse_drag(0)
crew one: key(f1)
crew to: key(f2)
cru three: key(f3)
cru for: key(f4)
crew five: key(f5)
cru six: key(f6)
crew seven: key(f7)
crew 8: key(f8)

pause: key(space)
(escape | back): key(escape)
<number_small>: key("{number_small}")
##,<user.letter>: key(letter)

#alt tab: user.window_tab()

# TODO alt-tab how to get working??
#alt tab: user.combo_key('alt', 'tab', .2)
#test: user.long_press('alt-enter', .2)

# ignore garbage
