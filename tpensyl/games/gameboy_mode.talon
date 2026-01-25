mode: user.gameboy
-
tag(): user.game_media
^(alt tab|altab| alt tabu)$:
    #prevent ahk button-mashing from cancelling next operation
    key(f24)
    user.window_tab()
    mode.disable("user.gameboy")
    mode.enable("command")
    #half the time focus doesn't work for code, just litters the logs with an air
    #user.switcher_focus("code")

focus <user.running_applications>: 
    user.switcher_focus(running_applications)
    user.mouse_move_center_active_window()
snap next [screen]: user.move_window_next_screen()

^screenshot$: key(f12)

^command mode$:
    mode.disable("user.gameboy")
    mode.disable("sleep")
    mode.enable("command")