mode: user.gameboy
win.title: /FTL: Faster Than Light/
app.exe: FTLGame.exe
-

#<phrase>: skip()

^jump$: key(j)
^ship$: key(u)
^(closed|clothes|close) doors$: key(x)
^return$: key(enter)
^drag$: user.mouse_drag(0)
(crew|cru) (1|on): key(f1)
(crew|cru) (2|to): key(f2)
(crew|cru) three: key(f3)
(crew|cru) (4|for): key(f4)
(crew|cru) five: key(f5)
(crew|cru) six: key(f6)
(crew|cru) seven: key(f7)
(crew|cru) eight: key(f8)
^(send|son)$: key(t)
^get$: key(r)
^cloak$: key(c)

(pause|stop): key(pgdown)
(escape | back): key(escape)
^one$: key('1')
^two$: key('2')
^three$: key('3')
^four$: key('4')
##,<user.letter>: key(letter)

#alt tab: user.window_tab()

# TODO alt-tab how to get working??
#alt tab: user.combo_key('alt', 'tab', .2)
#test: user.long_press('alt-enter', .2)

# ignore garbage