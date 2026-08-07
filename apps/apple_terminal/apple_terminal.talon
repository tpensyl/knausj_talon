app: apple_terminal
-
settings():
    # tpensyl - solving for weird keypress buffering? (5/8 was pretty stable)
    key_wait = 3
    key_hold = 5
    
# makes the commands in terminal.talon available
tag(): terminal

# use readline keybindings for various editing commands
tag(): user.readline

# activates the implementation of the commands/functions in terminal.talon
tag(): user.generic_unix_shell

# makes commands for certain applications available
# you can deactivate them if you do not use the application
tag(): user.git
# tag(): user.anaconda
# tag(): user.kubectl

tag(): user.tabs
tag(): user.file_manager

# tpensyl - not sure what these do, but resume was false firing.
# suspend: key(ctrl-z)
# resume:
#     insert("fg")
#     key(enter)
