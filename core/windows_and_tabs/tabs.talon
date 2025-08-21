tag: user.tabs
-
(tab|tabu) (open | new): app.tab_open()
(tab|tabu) new {user.website}: 
    app.tab_open()
    browser.go(website)
(tab|tabu) (last | previous | left): app.tab_previous()
(tab|tabu) left <number_small>: 
    app.tab_previous()
    repeat(number_small-1)
(tab|tabu) (next | right): app.tab_next()
(tab|tabu) right <number_small>: 
    app.tab_next()
    repeat(number_small-1)
(tab|tabu) close: user.tab_close_wrapper()
tab (force close|close force): user.tab_force_close()
tab (reopen | restore): app.tab_reopen()
go (tab|tabu) <number>: user.tab_jump(number)
go tab final: user.tab_final()
tab (duplicate | clone): user.tab_duplicate()

#TODO make more general for menu access and also mac specific
tab pin: 
    key(cmd-shift-/)
    sleep(10ms)
    "pin tab"
    key(down enter)

tab move left: user.tab_move_left()
tab move left <number_small>: 
    user.tab_move_left()
    repeat(number_small-1)
tab move right: user.tab_move_right()
tab move right <number_small>: 
    user.tab_move_right()
    repeat(number_small-1)
