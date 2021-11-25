-
# uncomment user.talon_populate_lists tag to activate talon-specific lists of actions, scopes, modes etcetera. 
# Do not enable this tag with dragon, as it will be unusable.
# with conformer, the latency increase may also be unacceptable depending on your cpu
# see https://github.com/knausj85/knausj_talon/issues/600
tag(): user.talon_populate_lists

talon check updates: menu.check_for_updates()
talon restart: user.exec("talon-restart")
talon open log: menu.open_log()
talon open rebel: menu.open_repl()
talon home: menu.open_talon_home()
talon copy context pie: user.talon_add_context_clipboard_python()
talon copy context: user.talon_add_context_clipboard()
talon copy name:
    name = app.name()
    clip.set_text(name)  
talon copy executable:
    executable = app.executable()
    clip.set_text(executable)
talon copy bundle:
    bundle = app.bundle()
    clip.set_text(bundle)
talon copy title: 
    title = win.title()
    clip.set_text(title)
talon dump version: 
    result = user.talon_version_info()
    print(result)
talon insert version: 
    result = user.talon_version_info()
    user.paste(result)
talon dump context: 
    result = user.talon_get_active_context()
    print(result)
^talon test last$:
    phrase = user.history_get(1)
    user.talon_sim_phrase(phrase)
^talon test numb <number_small>$:
    phrase = user.history_get(number_small)
    user.talon_sim_phrase(phrase)
^talon test <phrase>$:
    user.talon_sim_phrase(phrase)
# requires user.talon_populate_lists tag. do not use with dragon
^talon debug action {user.talon_actions}$: 
    user.talon_action_find("{user.talon_actions}")
# requires user.talon_populate_lists tag. do not use with dragon
^talon debug list {user.talon_lists}$:
    user.talon_debug_list(talon_lists)
# requires user.talon_populate_lists tag. do not use with dragon
^talon copy list {user.talon_lists}$:
    user.talon_copy_list(talon_lists)
^talon debug tags$:
    user.talon_debug_tags()
^talon debug modes$:
    user.talon_debug_modes()
# requires user.talon_populate_lists tag. do not use with dragon
^talon debug scope {user.talon_scopes}$:
    user.talon_debug_scope(talon_scopes)
# requires user.talon_populate_lists tag. do not use with dragon
^talon debug setting {user.talon_settings}$:
    user.talon_debug_setting(talon_settings)
^talon debug all settings$: 
    user.talon_debug_all_settings()
^talon debug active app$: 
    result = user.talon_get_active_application_info()
    print("**** Dumping active application **** ")
    print(result)
    print("***********************")
^talon copy active app$:
    result = user.talon_get_active_application_info()
    clip.set_text(result)
