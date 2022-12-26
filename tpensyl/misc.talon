# TODO list
# * octa shortcuts
# * get sublime tabs running
# * find in replace, find_and_replace
# * homophones.py can we add some order of precedent
# * one command to clear and oleate the line properly

start menu: key(super)

m v <user.number_string>: "MV-{number_string}"
big delta: "Δ"
epsilon: "ε"

north: edit.up()
#south: edit.down()

key: user.insert_between("key(", ")")
pop: mouse_click(1)
yap: "y\n" 

junk: key(backspace)
spamma: ", "
nope: edit.undo()
item: "* "
comma: ","
dot quote: "\""

vim save:
	key(esc)
	":wq\n"

go m v <user.number_string>:
	user.switcher_focus("chrome")
	app.tab_open()
	browser.go("https://bandwidth-jira.atlassian.net/browse/MV-{number_string}")

paste plain [text]: key(ctrl-shift-v)

