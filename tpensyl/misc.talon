# TODO list
# * octa shortcuts
# * get sublime tabs running
# * find in replace, find_and_replace
# * homophones.py can we add some order of precedent
# * one command to clear and oleate the line properly

 
m v <user.number_string>: "MV-{number_string}"
big delta: "Δ"
epsilon: "ε"

comma: ", "
nope: edit.undo()

pace: " "
vim save:
	key(esc)
	":wq\n"

go m v <user.number_string>:
	user.switcher_focus("chrome")
	app.tab_open()
	browser.go("https://bandwidth-jira.atlassian.net/browse/MV-{number_string}")