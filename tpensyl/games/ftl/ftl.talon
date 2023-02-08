mode: user.gameboy
win.title: /FTL: Faster Than Light/
app.exe: FTLGame.exe
-

settings():
    # minimum silence time (in seconds) before speech is cut off, default 0.3
    speech.timeout = 0.2
#<phrase>: skip()

^jump$: key(j)
^ship$: key(u)
^store$: key(s)
^(closed | clothes | close) doors$: key(x)
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
bring {user.ftl_crew}: 
    key(ftl_crew)
    mouse_click(1)

^(send|son)$: key(t)
^get$: key(r)
^cloak$: key(c)
^hack$: key(n) 
^mind control$: key(m)

(pause|stop): key(space)
(escape | back): key(escape)
^one$: key('1')
^two$: key('2')
^three$: key('3')
^four$: key('4')
shoot one: user.target_gun('1')
shoot two: user.target_gun('2')
shoot three: user.target_gun('3')
shoot four: user.target_gun('4')
shoot all:
    user.target_gun('1')
    user.target_gun('2')
    user.target_gun('3')
    user.target_gun('4')
