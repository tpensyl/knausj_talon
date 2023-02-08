mode: user.gameboy
-
tag(): user.game_media
^alt tab$:
    user.window_tab()
    mode.disable("user.gameboy")
    mode.enable("command")
    user.switcher_focus("code")