os: linux
-

settings():
    user.parrot_scroll_jump_size = 15

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
