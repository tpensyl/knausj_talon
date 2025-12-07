# tag: user.no_mouse
mode: all
-
mouse up: mouse_nudge(0,-10)
mouse up <number>:
    user.mouse_move(0,-10)
    repeat(number - 1)
mouse down: user.mouse_move(0,10)
mouse down <number>:
    user.mouse_move(0,10)
    repeat(number - 1)
mouse left: user.mouse_move(-10,0)
mouse left <number>:
    user.mouse_move(-10,0)
    repeat(number - 1)
mouse right: user.mouse_move(10,0)
mouse right <number>:
    user.mouse_move(10,0)
    repeat(number - 1)

mouse north:  user.mouse_move_window_relative(.5, .15)
mouse south:  user.mouse_move_window_relative(.5, .9)
mouse west:   user.mouse_move_window_relative(.1, .5)
mouse east:   user.mouse_move_window_relative(.9, .5)
mouse center: user.mouse_move_window_relative(.5, .45)

quad one: user.mouse_move_window_relative(.25, .25)
quad two: user.mouse_move_window_relative(.75, .25)
quad three: user.mouse_move_window_relative(.25, .75)
quad four: user.mouse_move_window_relative(.75, .75)