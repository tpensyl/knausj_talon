os: linux
-

settings():
    user.parrot_scroll_jump_size = 6
    user.whistle_scroll_speed = .015

(message clear|go away): 
    key(super-n)    
    key(esc)

screenshot unused:
    key(shift:down)
    sleep(100ms)
    key(printscr)
    sleep(100ms)
    user.mouse_drag(0)
    sleep(100ms)
    key(shift:up)
