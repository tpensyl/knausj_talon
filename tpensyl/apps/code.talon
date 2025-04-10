app: vscode
-

revert that: user.vscode("git.revertSelectedRanges")
stage that: user.vscode("git.stageSelectedRanges")
unstage that: user.vscode("git.unstageSelectedRanges")
key: user.insert_between("key(", ")")
# requires ext Git Blame by Wade Anderson
get blame: user.vscode("gitblame.quickInfo")

todo: "TODO "
todo <user.text>: "TODO {text}"
done: "DONE"