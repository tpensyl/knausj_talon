os: windows
-
# Can use this app from the Microsoft app store to set up hotkeys. 
# https://apps.microsoft.com/detail/9nblggh3zd5h?activetab=pivot%3Aoverviewtab&hl=en-us&gl=US

^screen standup$: key(ctrl-alt-w)
^screen (lie|lay) down$: key(ctrl-alt-a)
^screen refresh$: key(super-ctrl-shift-b)

# Hunt and Peck: Adds letter hotkeys to all visible UI elements, like rango for windows
# https://github.com/zsims/hunt-and-peck?tab=readme-ov-file
window (peck|pack)$: key(alt-;)
^(taskbar|bar) (peck|pack)$: key(ctrl-;)