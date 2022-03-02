#title: /Mathematica/

os: windows
app.exe: Mathematica.exe
-
#test: insert("test worked")

run [that]: key(shift-enter)
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

