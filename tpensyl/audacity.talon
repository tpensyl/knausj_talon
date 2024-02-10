app.app: /audacity.*/
-
play | pause | stop:        key(space)
export:      key(ctrl-shift-e)
file close: key(ctrl-w)
file close force: 
    key(ctrl-w)
    sleep(100ms)
    key(n)
file open: key(ctrl-o)
import audio: key(ctrl-shift-i)
(split delete | delete chunk): key(ctrl-alt-k)

zoom in: key(ctrl-1)
zoom out: key(ctrl-3)
select: key(f1)
move: key(f2)
# label:                      key(ctrl-b)
# step:                       skip()
# record:                     key(r)
# export selection:           key(ctrl-e)
