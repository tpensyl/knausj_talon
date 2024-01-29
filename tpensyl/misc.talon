# TODO list
# * octa shortcuts
# * get sublime tabs running
# * find in replace, find_and_replace

# * one command to clear and oleate the line properly

del: key(delete)

back: key(esc)
start menu: key(super)

m v <user.number_string>: "MV-{number_string}"
big delta: "Δ"
epsilon: "ε"

north: edit.up()
#south: edit.down()

(yap|yep): "y\n" 

junk: key(backspace)
spamma: ", "
nope: edit.undo()
item: "* "
dot quote: "\""

semicolon: ";"

vim save:
	key(esc)
	":wq\n"

go m v <user.number_string>:
	user.switcher_focus("chrome")
	app.tab_open()
	browser.go("https://bandwidth-jira.atlassian.net/browse/MV-{number_string}")

paste plain [text]: key(ctrl-shift-v)


^(boom|boon)$: mouse_click(1)

# TODO move to windows-only files
task manager: key(ctrl-shift-esc)

key(f1): speech.toggle()