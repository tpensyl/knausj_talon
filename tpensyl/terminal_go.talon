os: mac
-
# Focus (or launch) Terminal, open a new tab, cd. Runnable from any app.

tab new {user.terminal_dir}:
    user.switcher_launch("/System/Applications/Utilities/Terminal.app")
    app.tab_open()
    "cd {terminal_dir}\n"

claude new {user.terminal_dir}:
    user.switcher_launch("/System/Applications/Utilities/Terminal.app")
    app.tab_open()
    "cd {terminal_dir}\n"
    "claude\n"
