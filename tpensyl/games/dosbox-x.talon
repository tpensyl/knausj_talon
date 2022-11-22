mode: user.gameboy
win.title: /DOSBox-X.*/
-

^quick save now$: 
    user.quick_save()
    #for zork 
    key('backspace') 
    
^quick load now$:
    user.quick_load()

^next save slot$:
    user.next_slot()

^previous save slot$:
    user.previous_slot()

^toggle full screen$:
    user.toggle_full_screen()