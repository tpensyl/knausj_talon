tag: terminal
-

(sudo|pseudo): "sudo "
ansible vault view: "ansible-vault view " 
IP tables: "iptables "

diff: "diff "
diff so fancy: " -u|diff-so-fancy"

pip install: "pip install "
pip show: "pip show "
vscode: "code "
VPN: "vpn\n"
lisa <user.text>: "ls {text}"
lisa last: "ls -lastr\n"
katy up: "cd ..\n"
katy back: "cd -\n"
katy home: "cd ~\n"
katy that: 
    "cd "
    edit.paste()
    " \n"
katie text: "cd ~/txt\n"
katie source: "cd ~/src\n"
kitty var log: "cd /var/log\n"

quick build catapult: "quick-build-catapult\n"
v two cuddle start: "./v2ctl start\n"
v two cuddle start no app [service]: "./v2ctl start --no-app-service\n"
v two cuddle stop: "./v2ctl stop\n"
v two cuddle reset: "./v2ctl reset\n"

argo cuddle start: "./argoctl start\n"
argo cuddle stop: "./argoctl stop\n"
argo cuddle reset: "./argoctl reset\n"

move: "mv "
remove: "rm "
shell copy: "cp "
shell cat: "cat "
file find: "find -iname "
head: "head "
echo: "echo "
make der: "mkdir "
sublime: "subl "
grip: "|grep "
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
maven clean: "mvn clean \n"
maven clean install: "mvn clean install -T4 "
maven spring boot run: "mvn spring-boot:run -P developer"
maven dependency tree: "mvn dependency:tree "
maven check style: "mvn clean install -Dcobertura.skip -DskipTests  -T3 \n"
source AWS [connect]: "source aws-connect default"

my cat bin: "mycatbin\n"

(set | sit) title: "set-title "
(set | sit) title <user.text>: "set-title {text}\n"
#home: "~"
heroku: "heroku "
heroku login: "heroku login\n\n"

process list: "ps -aux"
process kill: "kill "
live tail: "tail -f "

system c t l: "systemctl "

# tmp macros. remove after!
# remove codeowners:
#     "git co master && g pull && rm CODEOWNERS && g a . && g diff --cached\n"
#     "g s\n"

# push new branch:
#     "git checkout -b MV-10393-remove-code-owners && g cm -m'MV-10393 remove CODEOWNERS' && git push --set-upstream origin MV-10393-remove-code-owners\n"
#     "g s\n"

# add missing tag:
#     "g cm --allow-empty -m'MV-10393' && g push\n"