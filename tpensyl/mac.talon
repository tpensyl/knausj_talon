os: mac
-
settings():
    user.whistle_scroll_speed = -1
    user.parrot_scroll_jump_size = -12
    user.help_max_command_lines_per_page = 40
    user.help_max_contexts_per_page = 22

# # currently 'key home' or 'key end' for the real keys
# home: key(cmd-left)
# end: key(cmd-right)

(home|head): edit.line_start()
(end|tail): edit.line_end() 

# TODO make a proper action instead of redefining command for each OS
paste plain [text]: key(cmd-shift-v)

menu: key(cmd-shift-/)
menu [<user.text>]: 
    key(cmd-shift-/)
    sleep(100ms)
    insert(text)
show hidden files: key(cmd-shift-.)

screenshot: key(cmd-shift-4)

# Bruno seems to require launch command instead of focus
focus bruno: user.switcher_launch("/Applications/Bruno.app")