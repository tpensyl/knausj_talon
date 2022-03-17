#title: /Mathematica/

os: windows
app.exe: Mathematica.exe
-
#test: insert("test worked")

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

run [that]:
    key(shift-enter)
    sleep(100ms)
    key(left:2)
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

