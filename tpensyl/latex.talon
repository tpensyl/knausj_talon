# tag: disabled
-
# latex shortcuts
greek alpha: "α"
greek beta: "β"
greek delta: "δ"
greek (big|cap) delta: "Δ"
greek epsilon: "ε"
greek gamma: "γ"
greek phi: "ϕ"
greek sigma: "σ"
greek theta: "θ"
greek omega: "ω"

unicode (cap|intersect): "∩"
unicode and: "∧"
unicode infinity: "∞"
unicode element [of]: "∈"

fake prob: user.insert_between("\\Pr[", "]")
fake expect: user.insert_between("\\E[", "]") 
fake epsilon: "\\eps"
fake omega: "\\omega"
fake eta: "\\eta"
fake sigma: "\\sigma"
fake delta: "\\delta"
fake gamma: "\\gamma"
fake (phi|fee): "\\phi"
(fake ell|fakle): "\\ell"
fake pi: "\\pi"
fake bar: "\\bar "
fake less [than] (equal|equals): "\\le "
fake greater [than] (equal|equals): "\\ge "
fake not (equal|equals): "\\ne "
fake not: "\\not "
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
fake (approx|approximate): "\\approx "
fake gets: "\\gets "
fake see dot: "\\cdot "
fake some: user.insert_between("\\sum_{", "}")
fake left: "\\left"
fake right: "\\right"
fake for all: "\\forall "
fake exists: "\\exists "
fake tilde: "\\tilde "
fake lore: "\\lor "
fake [set] (intersect|intersection): "\\cap "
fake [set] union: "\\cup "
fake big cup: user.insert_between("\\bigcup_{", "}")
fake set minus: "\\setminus "
fake subset: "\\subset "
fake subset (equal|equals): "\\subseteq "
# custom command
fake vector sum: "\\vsum "
fake (textile | text style): "\\textstyle"
#High potential for unwanted matches
#fake <user.word>:
	#"\\{user.word} "
fake square root: user.insert_between("\\sqrt{", "}")
fake subsection: user.insert_between("\\subsection{", "}")
fake subsubsection: user.insert_between("\\subsubsection{", "}")
fake label: user.insert_between("\\label{", "}")
fake (tommy | tea note): user.insert_between("\\Tnote{", "}")

(empty|inside) fake (brace|braces): user.insert_between("\\{", "\\}")
(empty|inside) math: user.insert_between("$", "$")
fake mid: "\\mid "

ceiling that: 
    text = edit.selected_text()
    user.paste("\\lceil {text} \\rceil")

floor that: 
    text = edit.selected_text()
    user.paste("\\lfloor {text} \\rfloor")

dollar wrap <user.cursorless_target>:
	user.cursorless_command("editNewLineAfter", cursorless_target)
	"\"\"\"\"\"\""
	key(left:3)

#  <user.cursorless_target>:
# 	text = user.cursorless_get_text(cursorless_target)