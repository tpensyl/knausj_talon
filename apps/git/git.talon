tag: terminal
and tag: user.git
-
git add dot: "git add . \n"
git amend: "git commit --amend"
git branch delete: "git branch -D "
git checkout branch: "git checkout -b "
git checkout origin [slash] master: "git checkout origin/master\n"
git commit message:
    "git commit -m ''"
    key(left)

git commit [allow] empty:
    "git commit --allow-empty -m''"
    key(left)
git show head: "git show HEAD"


git {user.git_command} [<user.git_arguments>]:
    args = git_arguments or ""
    "git {git_command}{args} "
git commit [<user.git_arguments>] message [<user.prose>]:
    args = git_arguments or ""
    message = prose or ""
    user.insert_between("git commit{args} --message '{message}", "'")
git stash [push] [<user.git_arguments>] message [<user.prose>]:
    args = git_arguments or ""
    message = prose or ""
    user.insert_between("git stash push{args} --message '{message}", "'")

# Optimistic execution for frequently used commands that are harmless (don't
# change repository or index state).
git status$: "git status \n"
git add patch$: "git add --patch \n"
git show head$: "git show HEAD \n"

git diff$: "git diff \n"
git diff (cached | cashed)$: "git diff --cached \n"
git log$: "git log \n"

git checkout dot$: "git checkout . \n"
# Not sure how much this helps yet
git checkout <user.text>$: "git checkout {text}\t"

git add dot$: "git add . \n"
git push$: "git push \n"
git pull$: "git pull \n"
git fetch$: "git fetch \n"
git stash$: "git stash \n"
git stash pop$: "git stash pop \n"

git commit allow empty: 
    "git commit --allow-empty -m''"
    key(left)

# Convenience
git clone clipboard:
    insert("git clone ")
    edit.paste()
    key(enter)
git diff highlighted:
    edit.copy()
    insert("git diff ")
    edit.paste()
    key(enter)
git diff clipboard:
    insert("git diff ")
    edit.paste()
    key(enter)
git add highlighted:
    edit.copy()
    insert("git add ")
    edit.paste()
    key(enter)
git add clipboard:
    insert("git add ")
    edit.paste()
    key(enter)
git commit highlighted:
    edit.copy()
    insert("git add ")
    edit.paste()
    insert("\ngit commit\n")
