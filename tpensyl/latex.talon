tag: disabled
-
# latex shortcuts
(phi|fee): "ϕ"
big delta: "Δ"
delta: "δ"
epsilon: "ε"

fake prob: user.insert_between("\\Pr[", "]")
fake expect: user.insert_between("\\E[", "]") 
fake epsilon: "\\eps"
fake (phi|fee): "\\phi"
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
fake begin: user.insert_between("\\begin{", "}")
fake end <user.word>:
	"\\end{{{user.word}}}"
fake end: user.insert_between("\\end{", "}")
fake item:
	"\\item "
fake emf: user.insert_between("\\emph{", "}")
fake infinity:
	"\\infty "
#High potential for unwanted matches
#fake <user.word>:
	#"\\{user.word} "
fake square root: user.insert_between("\\sqrt{", "}")
fake subsection: user.insert_between("\\subsection{", "}")
fake subsubsection: user.insert_between("\\subsubsection{", "}")
fake label: user.insert_between("\\label{", "}")
fake tommy: user.insert_between("\\tommy{", "}")

