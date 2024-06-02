#title: /Mathematica/
os: windows
app.exe: Mathematica.exe
-
#test: insert("test worked")

more: key(ctrl-.)
brick: ';'

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

box top:
    key(shift-up:50)
    key(left)

box bottom:
    key(shift-down:50)
    key(right)

copy (cell | box):
    key(shift-up:50)
    key(up)
    key(down)
    key(shift-down:50)
    edit.copy()

(take | select) (cell | box):
    key(shift-up:50)
    key(up)
    key(down)
    key(shift-down:50)

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

(cell | box) (delete | del):
    key(shift-up:50)
    key(up)
    key(shift-down)
    key(delete)
    key(down)

[cell | box] (expand | collapse | open | close): key(ctrl-')

(cell run | box run | run that | hard slap):
    key(shift-enter)
    sleep(500ms)
    #key(left)
    key(right:2)
    # key(shift-up:50)
    # key(up:2)

box stop: key(alt-.)

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

(inside dub squares)|index:
    user.insert_between("[[","]]")

funk table: user.insert_between("Table[",",{}]")
funk men: user.insert_between("Min[","]")
funk max: user.insert_between("Max[","]")

funk map: "/@"
replace: user.insert_between("/.{","}")

args: user.insert_between("[","]")

post simplify: "//Simplify"
post full simplify: "//FullSimplify"
slash at: "/@"