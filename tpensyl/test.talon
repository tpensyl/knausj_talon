mode: all
#tag: user.debug_widget
# tag: disabled
-
tag(): user.debug_widget
move debug <number>: user.set_debug_coordinates(number, number)
debug <user.text>: user.set_debug_text("{text}")
#hack <user.text>: user.set_debug_text(3)
#vyeet <number>: 
stopwatch start: user.start_stopwatch()
stopwatch stop: user.set_debug_text("")
 
look upper: user.start_mouse_move_up()
look downer: user.start_mouse_move_down()
look stop: user.stop_mouse_move() 
auto run: user.system_command_nb("C:\\games\\ahk-scripts\\bstone.ahk") 
auto stop: key(f24) 

copy down <number>:
    edit.line_start()
    #e.g. include indentation of first line
    edit.line_start() 
    edit.extend_line_down()
    repeat(number- 1)

test down <number>:
    key(home:2)
    key('shift-down:{number-1}')
    key(shift-end)