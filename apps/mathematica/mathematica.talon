#title: /Mathematica/

os: windows
app.exe: Mathematica.exe
-
#test: insert("test worked")

run that: key(shift-enter)
square root: 
	insert("Sqrt[]")
	key(left)

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
    

#workspace <number>: key("ctrl-{number}")

#(slack | lack) [channel] info: key(ctrl-shift-i)

#focus (move | next): key(ctrl-`)
#(section | zone) [next]: key(f6)
#(section | zone) (previous | last): key(shift-f6)
