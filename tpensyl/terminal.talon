tag: terminal
-

VPN: "vpn\n"
lisa <user.text>: "ls {text}"
katy up: "cd ..\n"
katy back: "cd -\n"
katy home: "cd ~\n"
move: "mv "
remove: "rm "
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
h top: "htop\n"
find name:
	"find -name *"
	key(left)
sudo: "sudo "

maven: "mvn "

(set | sit) title: "set-title "
(set | sit) title <user.text>: "set-title {text}\n"
#home: "~"
heroku: "heroku "
