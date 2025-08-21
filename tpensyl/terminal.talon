tag: terminal
-

(sudo|pseudo): "sudo "
ansible vault view: "ansible-vault view " 
IP tables: "iptables "

docker list: "docker ps\n"

diff: "diff "
diff so fancy: " -u|diff-so-fancy"

pip install: "pip install "
pip show: "pip show "
vscode: "code "
VPN: "vpn\n"
lisa <user.text>: "ls {text}"
lisa last: "ls -lastr\n"
# katy up: "cd ..\n"
# katy back: "cd -\n"
katy home: "cd ~\n"
katy that: 
    "cd "
    edit.paste()
    " \n"
# katie text: "cd ~/txt\n"
# katie source: "cd ~/src\n"
kitty var log: "cd /var/log\n"

brew install: "brew install "

quick build catapult: "quick-build-catapult\n"
quick build argo: "mvn clean install  -Dos.arch=x86_64 -DunitTests.skip -DsmokeTests.skip -DintegrationTests.skip\n"
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
    "grep -rI '' ."
    key(left:3)
recursive grip <user.text>:
    "grep -rI '{text}' ."
    key(left:3)
recursive grip that:
    "grep -rI '"
    edit.paste()
    "' .\n"
grip word:
    "grep -rI -w '' ."
    key(left:3)
h top: "htop\n"
find name:
    "find -name *"
    key(left)
sudo: "sudo "
maven: "mvn "
maven clean: "mvn clean \n"
maven clean install: "mvn clean install -T4 \n"
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

process list: "ps -ax"
process kill: "kill "
live tail: "tail -f "

system c t l: "systemctl "

java (environment|env): "jenv "

# tmp macros. remove after!
# remove codeowners:
#     "git co master && g pull && rm CODEOWNERS && g a . && g diff --cached\n"
#     "g s\n"

# push new branch:
#     "git checkout -b MV-10393-remove-code-owners && g cm -m'MV-10393 remove CODEOWNERS' && git push --set-upstream origin MV-10393-remove-code-owners\n"
#     "g s\n"

# add missing tag:
#     "g cm --allow-empty -m'MV-10393' && g push\n"