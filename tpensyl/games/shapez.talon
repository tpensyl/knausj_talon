mode: user.gameboy
and app.name: shapez
-
#puzzle: WyRc--Rc:----Wy--
#buffer
#multiplex 1: " RcRcRcRc:CcCcCcCc:------Sy"
#multiplex 2: RcRcRcRc:CcCcCcCc:Sy------
#multiplex 2: RcRcRcRc:CcCcCcCc:--Sy----
#multiplex 4: traffic light: WgWgWgWg:WyWyWyWy:WrWrWrWr
settings():
    speech.timeout = 0.15
    user.hiss_scroll_debounce_time = 100
    user.whistle_scroll_speed = .02
    key_wait = 30

say <phrase>: insert(phrase)

zoom in: key(+:10)
zoom out: key(-:10)

(bacca): key(esc)
upgrade: key(f)
(rev revrr|mode): key(t)
grab: user.drag_with_modifier(0, 'ctrl')
many: user.set_hold('shift', true)

belt: key(1)
(merger|splitter|crossing): key(2)
(tunnel|bridge|constant|signal): key(3)
extractor: 
    user.set_hold('shift', true)
    key(4)
cutter: key(5)
rotator: key(6)
stacker: key(7)
(mixer|transistor): key(8)
painter: key(9)
garbage: key(0)
storage: key(y)
meter: key(u)
switch: key(i)
filter: key(o)
display: key(p)

wires: key(e)
# wire: key(1)

carve: key(x)
copy: key(c)
paste: key(v)
delete: key(del)
clear: key(b)
clone: key(q)
marker: key(m)


junk: key(del)

# reverse: hold alt
# ctrl-drag to select area