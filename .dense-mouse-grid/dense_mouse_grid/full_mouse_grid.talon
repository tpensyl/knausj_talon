tag: user.full_mouse_grid_enabled
-
dense [mouse] grid$:
    user.full_grid_close()
    user.full_grid_activate()
    user.rango_force_explicit_clicking()

dense [mouse] grid screen <number>:
    user.full_grid_close()
    user.full_grid_select_screen(number)

dense [mouse] grid win:
    user.full_grid_close()
    user.full_grid_place_window()

 