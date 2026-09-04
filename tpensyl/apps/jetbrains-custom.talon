app: jetbrains
# and code.language: /.+/
-

# tuned for mac at work
settings():
    user.parrot_scroll_jump_size = -50

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
file copy name: user.idea("action CopyFileName")
file copy path: user.idea("action CopyAbsolutePath")
file copy local [path]: user.idea("action CopyPathFromRepositoryRootProvider")
file copy line: user.idea("action CopyPathWithLineNumber")

copilot: user.idea("action copilot.requestCompletions")
yes: key(tab)

# run that: key("shift-f10") (linux)
go source: key(f4)
run that: key("ctrl-f5")

# neither of these work
# git history: user.idea("Git.Log")
# git show history: user.idea("action Git.FileHistory.ContextMenu")
# git history: user.idea("action Vcs.ShowHistoryForBlock")
git compare branch: user.idea("action Git.CompareWithBranch")
# git show history selected: user.idea("action Compare.Selected")
# git show history: user.idea("action Compare.Specified")


#TODO find the action id. This it requires custom shortcut:
vault edit: key(ctrl-alt-shift-z)
diff next: key(cmd-alt-i)
stage:
    key(ctrl-cmd-left)
    sleep(15ms)
    key(cmd-alt-i)
unstage:
    key(ctrl-cmd-right)
    sleep(15ms)
    key(cmd-alt-i)
file next:
    key(ctrl-shift-right)
file last:
    key(ctrl-shift-left)
to do: "//TODO tpensyl "

# can find action e2es by installing/enabling ideaVim. then type  :actionlist

# Requires TabMover plugin
# git.MainMenu.FileActions
