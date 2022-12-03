mode: user.gameboy
win.title: /.*DOSBox.*ZORK.*/
-

#settings():
#speech.timeout = .2

go up: "go up\n"
go down: "go down\n"
go (south | self): "go south\n"
go southeast: "go southeast\n"
go southwest: "go southwest\n"
go north: "go north\n"
go northeast: "go northeast\n"
go northwest: "go northwest\n"
go east: "go east\n"
go west: "go west\n"
inventory: "inventory\n"
help: "look\n"

take <phrase>$: "take {phrase}"
examine <phrase>$: "examine {phrase}"
pull <phrase>$: "pull {phrase}"

# bring minimal editing commands
pad: key(space)
junk: key('backspace')
junk <number_small>: key('backspace:{number_small}')
clear line: key('backspace:100')
word <user.word>: user.insert_formatted(user.word, "NOOP")
<user.letter>: key(letter)
look around: "look\n"

# dictation
<phrase>$: insert(phrase)
