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
item: "* "
pause: ","


vim save:
	key(esc)
	":wq\n"

go m v <user.number_string>:
	user.switcher_focus("chrome")
	app.tab_open()
	browser.go("https://bandwidth-jira.atlassian.net/browse/MV-{number_string}")

fake prob: 
	"\\Pr[]"
	key(left)
fake expect: 
	"\\E[]"
	key(left)
fake epsilon: "\\eps"
fake bar: "\\bar "
fake less [than] (equal|equals): "\\le "
fake greater [than] (equal|equals): "\\ge "
fake not (equal|equals): "\\ne "
#fake in: "\\in "
fake ref: 
	"\\ref{}"
	key(left)
fake cite: 
	"\\cite{}"
	key(left)
fake (frack | fraction):
	"\\frac{}"
	"{}"
	key(left:3)
fake begin:
	"\\begin{}"
	key(left)
fake end:
	"\\end{}"
	key(left)
fake item:
	"\\item "
fake emf:
	"\\emph{}"
	key(left)
fake infinity:
	"\\infty "
fake <user.word>:
	"\\{user.word} "
fake square root:
	"\\sqrt{}"
	key(left)