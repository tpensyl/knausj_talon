title: /.*budget.*Excel/
title: /.*LibreOffice Calc/
-

# LibreOffice kept jumbling words
settings():
    key_wait = 2

slap: key(enter)
[go] down: key(down)
[go] up: key(up)
[go] left: key(left)
[go] right: key(right)

comment edit: key(shift-f2)
comment delete:
    key(shift-f10)
    key(m)
comment close:
    key(esc)
    key(esc)

edit: key(f2)
start [entry]:
    key(f2)
    "="
add [entry]:
    key(f2)
    "+"
