# tag: disabled
-
# latex shortcuts
(phi|fee): "ϕ"
omega: "ω"
big delta: "Δ"
delta: "δ"
epsilon: "ε"

fake prob: user.insert_between("\\Pr[", "]")
fake expect: user.insert_between("\\E[", "]") 
fake epsilon: "\\eps"
fake omega: "\\omega"
fake eta: "\\eta"
fake sigma: "\\sigma"
fake (phi|fee): "\\phi"
fake pi: "\\pi"
fake bar: "\\bar "
fake less [than] (equal|equals): "\\le "
fake greater [than] (equal|equals): "\\ge "
fake not (equal|equals): "\\ne "
#fake in: "\\in "
fake ref: user.insert_between("\\ref{", "}") 
fake cite: user.insert_between("\\cite{", "}") 
fake (frack | fraction): user.insert_between("\\frac{", "}{}")
fake (begin|began) <user.word>:
	"\\begin{{{user.word}}}"
fake (begin|began) (align|aline): "\\begin{{align*}}"
fake end (align|aline): "\\end{{align*}}"
fake begin: user.insert_between("\\begin{", "}")
fake end <user.word>:
	"\\end{{{user.word}}}"
fake end: user.insert_between("\\end{", "}")
fake item:
	"\\item "
fake emf: user.insert_between("\\emph{", "}")
fake infinity:
	"\\infty "
fake in: "\\in "
fake approx: "\\approx "
fake see dot: "\\cdot "
fake some: "\\sum_{}"
fake left: "\\left"
fake right: "\\right"
fake (textile | text style): "\\textstyle"
#High potential for unwanted matches
#fake <user.word>:
	#"\\{user.word} "
fake square root: user.insert_between("\\sqrt{", "}")
fake subsection: user.insert_between("\\subsection{", "}")
fake subsubsection: user.insert_between("\\subsubsection{", "}")
fake label: user.insert_between("\\label{", "}")
fake (tommy | tea note): user.insert_between("\\Tnote{", "}")

ceiling that: 
    text = edit.selected_text()
    user.paste("\lceil {text} \\rceil")

dollar wrap <user.cursorless_target>:
	user.cursorless_command("editNewLineAfter", cursorless_target)
	"\"\"\"\"\"\""
	key(left:3)

#  <user.cursorless_target>:
# 	text = user.cursorless_get_text(cursorless_target)