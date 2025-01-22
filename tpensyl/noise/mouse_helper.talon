
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