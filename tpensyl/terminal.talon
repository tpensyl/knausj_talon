tag: terminal
-

vscode: "code "
VPN: "vpn\n"
lisa <user.text>: "ls {text}"
lisa last: "ls -lastr\n"
katy up: "cd ..\n"
katy back: "cd -\n"
katy home: "cd ~\n"
move: "mv "
remove: "rm "
shell copy: "cp "
shell cat: "cat "
shell cat <user.text>: "cat {text}"
head: "head "
echo: "echo "
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
grip word:
	"grep -r -w '' ."
	key(left)
	key(left)
	key(left)
h top: "htop\n"
find name:
	"find -name *"
	key(left)
sudo: "sudo "
maven: "mvn "
maven clean install: "mvn clean install"
maven spring boot run: "mvn spring-boot:run"
source AWS connect: "source aws-connect default"

my cat bin: "mycatbin\n"

(set | sit) title: "set-title "
(set | sit) title <user.text>: "set-title {text}\n"
#home: "~"
heroku: "heroku "
heroku login: "heroku login\n\n"
