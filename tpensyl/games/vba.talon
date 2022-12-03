mode: user.gameboy
and win.title: /.*VisualBoyAdvance.*/
-

settings():
    # minimum silence time (in seconds) before speech is cut off, default 0.3
    speech.timeout = 0

up:
    key(up:down)
    sleep(128ms)
    key(up:up)
down:
    key(down:down)
    sleep(128ms)
    key(down:up)
left:
    key(left:down)
    sleep(128ms)
    key(left:up)
right:
    key(right:down)
    sleep(128ms)
    key(right:up)
start:
    key(enter:down)
    sleep(32ms)
    key(enter:up)
select:
    key(backspace:down)
    sleep(32ms)
    key(backspace:up)
b:
    key(a:down)
    sleep(32ms)
    key(a:up)
(speed | turbo): key(t)
