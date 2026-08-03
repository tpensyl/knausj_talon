app: apple_terminal
win.title: /[Cc]laude/
-
claude model <user.word>: "/model {word}\n"
claude model: "/model \n"
claude cost: "/cost\n"
claude rewind: "/rewind\n"
claude context: "/context\n"
(claude kill | claude close):
    key(escape)
    sleep(40ms)
    key(ctrl-c)
    "/exit\n"
    sleep(1100ms)
    app.tab_close()
details: key(ctrl-o)

#(submit | send | run it): key(enter)
#(interrupt | stop | escape it): key(escape)
# abort:
#     key(escape)
#     sleep(30ms)
#     key(escape)

# shift-tab cycles Claude's mode (normal / auto-accept / plan)
(cycle mode | mode next): key(shift-tab)
