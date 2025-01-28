os: windows
app.name: /^Wolfram Mathematica/
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

(cell | box) copy:
    key(shift-up:50)
    key(up)
    key(down)
    key(shift-down:50)
    edit.copy()

(cell | box) (take | select):
    key(shift-up:50)
    key(up)
    key(down)
    key(shift-down:50)

(cell | box) draft:
    key(shift-up:50)
    key(up)
    key(down)
    key(shift-down:50)
    sleep(300ms)
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

(cell run | box run | run that | hard slap | compile):
    key(shift-enter)
    sleep(500ms)
    #key(left)
    key(right:2)
    # key(shift-up:50)
    # key(up:2)

box stop: key(alt-.)

funk square root:
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
funk plot: user.insert_between("Plot[",",{{}}]")
funk plot three d: user.insert_between("Plot3D[",",{{}},{{}}]")

funk map: "/@"
replace: "/."
replace with: user.insert_between("/.{","}")

args: user.insert_between("[","]")

post simplify: "//Simplify"
post full simplify: "//FullSimplify"
post together: "//Together"
slash at: "/@"