mode: user.gameboy
and app.name: shapez
-

settings():
    speech.timeout = 0.15
    user.hiss_scroll_debounce_time = 100
    user.whistle_scroll_speed = .02
    key_wait = 30

zoom in: key(+:10)
zoom out: key(-:10)

(bacca): key(esc)
upgrade: key(f)
(rev revrr|mode): key(t)
grab: user.drag_with_modifier(0, 'ctrl')
many: user.set_hold('shift', true)

belt: key(1)
(merger|splitter): key(2)
(tunnel|bridge): key(3)
extractor: 
    user.set_hold('shift', true)
    key(4)
cutter: key(5)
rotator: key(6)
stacker: key(7)
mixer: key(8)
painter: key(9)
garbage: key(0)
storage: key(y)

cut: key(x)
copy: key(c)
paste: key(v)
delete: key(del)
clear: key(b)
clone: key(q)

junk: key(del)

# reverse: hold alt
# ctrl-drag to select area