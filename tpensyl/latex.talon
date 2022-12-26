tag: disabled
-
# latex shortcuts
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
#High potential for unwanted matches
fake <user.word>:
	"\\{user.word} "
fake square root:
	"\\sqrt{}"
	key(left)
