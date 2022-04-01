#title: /Mathematica/

os: windows
app.exe: Mathematica.exe
-
#test: insert("test worked")

more: key(ctrl-.)

go top:
    edit.file_start()
    key(right)

go bottom:
    edit.file_end()
    key(left)

exit down:
	key(shift-down:50)
    key(down)

exit up:
    key(shift-up:50)
    key(up)

(take | select) (cell | box):
    key(shift-up:50)
    key(up)
    key(down)
    key(shift-down:50)
    edit.copy()

draft (cell | box):
    key(shift-up:50)
    key(up)
    key(down)
    key(shift-down:50)
    user.draft_editor_open()

(cell | box) down:
    # key(right)
    key(shift-down:50)
    key(down:2)

(cell | box) up:
    # key(left)
    key(shift-up:50)
    key(up:2)

cell (delete | del):
    key(shift-up:50)
    key(up)
    key(shift-down)
    key(delete)
    key(down)

(run [that] | hard slap):
    key(shift-enter)
    sleep(500ms)
    #key(left)
    key(right:2)
    # key(shift-up:50)
    # key(up:2)

square root: 
	insert("Sqrt[]")
	key(left)
times: "*"

comment line:
    edit.select_line()
    key(alt-/)

inside comment:
    insert("(*  *)")
    key(left)
    key(left)
    key(left)

inside (dub|double) squares:
	insert("[[]]")
	key(left)
    key(left)

