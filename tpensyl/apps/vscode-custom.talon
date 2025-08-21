app: vscode
-

# cd /Users/tpensyl/Library/"Application Support"/JetBrains/IntelliJIdea2024.3
# grep -rI 'shift ctrl alt z' .
# grep -rI 'shift ctrl alt Z' .

# grep -rI 'shift ctrl alt' .

# tuned for work mac
settings():
    user.parrot_scroll_jump_size = -15

tag(): terminal
tag(): user.git

# Helpful commands from vscode.talon:
# terminal trash
# focus editor
# terminal one

revert that: user.vscode("git.revertSelectedRanges")
stage that: user.vscode("git.stageSelectedRanges")
unstage that: user.vscode("git.unstageSelectedRanges")
key: user.insert_between("key(", ")")
# requires ext Git Blame by Wade Anderson
get blame: user.vscode("gitblame.quickInfo")

# TODO remove these after updating community
accept current: user.vscode("merge-conflict.accept.current")
accept incoming: user.vscode("merge-conflict.accept.incoming")
accept both: user.vscode("merge-conflict.accept.both")
conflict next: user.vscode("merge-conflict.next")
conflict last: user.vscode("merge-conflict.previous")

todo: "TODO "
todo <user.text>: "TODO {text}"
done: "DONE"

bash that:
    key(cmd-c)
    user.vscode("workbench.action.terminal.focus")
    sleep(200ms)
    key(cmd-v)
    key(enter)

bash <user.cursorless_target>:
    x = user.cursorless_get_text(cursorless_target)
    user.vscode("workbench.action.terminal.focus")
    insert(x)
    key(enter)

bring <user.cursorless_target> to <user.running_applications>:
    x = user.cursorless_get_text(cursorless_target)
    user.switcher_focus(running_applications)
    insert(x)