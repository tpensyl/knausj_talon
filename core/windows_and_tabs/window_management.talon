window (new | open): app.window_open()
window next: app.window_next()
window last: app.window_previous()
window close: app.window_close()
window hide: app.window_hide()
app (preferences | prefs | settings): app.preferences()
focus <user.running_applications>: 
    user.switcher_focus(running_applications)
    user.mouse_move_center_active_window()
# following only works on windows. Can't figure out how to make it work for mac. No idea what the equivalent for linux would be.
^focus all$: user.switcher_menu()
focus last: 
    user.switcher_focus_last()
    user.mouse_move_center_active_window()
running list: user.switcher_toggle_running()
running close: user.switcher_hide_running()
[talon] launch <user.launch_applications>: user.switcher_launch(launch_applications)

snap <user.window_snap_position>: user.snap_window(window_snap_position)
snap next [screen]:
    user.move_window_next_screen()
    sleep(10ms)
    user.mouse_move_center_active_window()
snap last [screen]:
    user.move_window_previous_screen()
    user.mouse_move_center_active_window()
snap screen <number>: user.move_window_to_screen(number)
snap <user.running_applications> <user.window_snap_position>:
    user.snap_app(running_applications, window_snap_position)

snap <user.running_applications> [screen] <number>:
    user.move_app_to_screen(running_applications, number)
