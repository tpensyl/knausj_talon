mode: user.gameboy
and app.name: Borderlands 2
-
settings():
    speech.timeout = 0.1
    user.hiss_scroll_debounce_time = 200
    # key_wait = 10
    # key_hold = 30

^(bacca)$: key(esc)
^(enter|slap)$: key(enter)
^stuff$: key(tab)

^run$: key(shift)
^jump$: key(space)
^next$: key([)
^reload$: key(r)
^smack$: key(v)
^turret$: key(f)
^grenade$: key(g)
^(shop|drop)$: key(q)
^honk$: key(z)

^grab$: 
    key(e:down)
    sleep(600ms)
    key(e:up)


^backpedal$: user.set_hold('s', true)
^drive mode$: user.drive_mode_on()

#^<phrase>$: skip()