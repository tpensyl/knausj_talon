tag: terminal
-

lisa <user.text>: "ls {text}"
move: "mv "
copy: "cp "
cat: "cat "
cat <user.text>: "cat {text}"
make der: "mkdir "
sublime: "subl "
grip: "grep "
recursive grip: 
	"grep -r '' ."
 	key(left)
 	key(left)
 	key(left)
recursive grip <user.text>:
	"grep -r '{text}' ."
 	key(left)
 	key(left)
 	key(left)
recursive grip that:
	"grep -r '"
	edit.paste()
	"' .\n"
