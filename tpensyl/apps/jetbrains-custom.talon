app: jetbrains
# and code.language: /.+/
-

# tuned for mac at work
settings():
    user.parrot_scroll_jump_size = -60

replace it: key(cmd-alt-f)
hunt case: key(alt-c)
hunt word: key(alt-w)
hunt regex: key(alt-x)
file locate: key(alt-f1 1)
(rap|wrap) switch: key(alt-z)

#e.g. key(alt-enter)
show fix: user.idea("action ShowIntentionActions")
show folder: user.idea("action ProjectView.AutoscrollFromSource")
project build: user.idea("action CompileProject")

copilot: user.idea("copilot.requestCompletions")
yes: key(tab)

# run that: key("shift-f10") (linux)
run that: key("ctrl-f5")
git history: user.idea("Git.Log")

#TODO find the action id. This it requires custom shortcut:
vault edit: key(ctrl-alt-shift-z)

# can find action e2es by installing/enabling ideaVim. then type  :actionlist

# Requires TabMover plugin
