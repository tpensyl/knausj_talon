os: windows
-

settings():
    user.parrot_scroll_jump_size = 15

# Can use this app from the Microsoft app store to set up hotkeys. 
# https://apps.microsoft.com/detail/9nblggh3zd5h?activetab=pivot%3Aoverviewtab&hl=en-us&gl=US
# TODO how to run on startup

# TODO make a proper action instead of redefining command for each OS
paste plain [text]: key(ctrl-shift-v)

^screen standup$: key(ctrl-alt-w)
^screen (lie|lay) down$: key(ctrl-alt-a)
^screen (lie|lay) down reverse$: key(ctrl-alt-d)

# Helps if second monitor stops working after sleep
^talon fix screen$: key(super-ctrl-shift-b)

# Hunt and Peck: Adds letter hotkeys to all visible UI elements, like rango for windows
# https://github.com/zsims/hunt-and-peck?tab=readme-ov-file
window (peck|pack)$: key(alt-;)
^(taskbar|bar) (peck|pack)$: key(ctrl-;)

# This worked on windows 11 to have "configure" open CSV in vscode
# HKEY_CLASSES_ROOT\SystemFileAssociations\text\shell\edit\command
# ORIGINAL: %SystemRoot%\system32\NOTEPAD.EXE %1
# NEW: code.cmd %1