mode: user.gameboy
and app.name: Talos
-

settings():
    speech.timeout = 0.2
    
    #key_hold = 100.0
    #key_wait = 100.0

pogo: user.set_talos_tertiary_noise_action("jump")
alt use mode: user.set_tertiary_noise_action("alt-use")

use: mouse_click(0)
curdle: mouse_click(1)
third person: key(h)
^reset puzzle$: key(x)
journal: key(tab)
jump: key(space)
back: key(esc)
    # key(esc:down)
    #         sleep(100ms)
    # key(esc:up)
sprint: user.toggle_hold('shift')
backpedal:
    user.set_hold('down', true)
screenshot: key(f12)

#^<phrase>$: skip()