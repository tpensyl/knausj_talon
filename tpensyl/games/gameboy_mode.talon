mode: user.gameboy
-
tag(): user.game_media
^alt tab$:
    user.window_tab()
    mode.disable("user.gameboy")
    mode.enable("command")
    #half the time focus doesn't work for code, just litters the logs with an air
    #user.switcher_focus("code")

^screenshot$: key(f12)