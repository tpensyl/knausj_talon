tag: terminal
-
# tags should be activated for each specific terminal in the respective talon file

lisa: user.terminal_list_directories()
lisa all: user.terminal_list_all_directories()
katie$: "cd "
katie <user.text> slap$: "cd {text}\t\n"
katie <user.text>$: "cd {text}\t"
katie <user.letter>: "cd {letter}\t"
katie dot <user.text>: "cd .{text}\t"
    #user.terminal_change_directory(text or "")
katie root: user.terminal_change_directory_root()
katie up: user.terminal_change_directory("..")
#impl specific
katie back: user.terminal_change_directory("-")

katie source: user.terminal_change_directory("src")

go <user.system_path>: insert('cd "{system_path}"\n')
path <user.system_path>: insert('"{system_path}"')
clear screen: user.terminal_clear_screen()
run last: user.terminal_run_last()
rerun [<user.text>]: user.terminal_rerun_search(text or "")
rerun search: user.terminal_rerun_search("")
kill all: user.terminal_kill_all()

copy paste:
    edit.copy()
    sleep(50ms)
    edit.paste()

vim : "vim "
vim <user.text>$: "vim {text}\t"