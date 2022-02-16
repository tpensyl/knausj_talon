from talon import Context, Module, actions, imgui, settings, ui, app, ctrl

ctx = Context()
mod = Module()
ctx.matches = r"""
app: windows_power_shell
app: windows_terminal
and win.title: /PowerShell/
"""

directories_to_remap = {}
directories_to_exclude = {}

@ctx.action_class('edit')
class EditActions:
    def delete_line():
        actions.insert(' ')
        actions.key('esc')
    #def paste(): ctrl.mouse_click(button=1)

@ctx.action_class('user')
class UserActions:
    def file_manager_refresh_title():
        actions.insert("$Host.UI.RawUI.WindowTitle = 'Windows PowerShell: ' +  $(get-location)")
        actions.key('enter')
        #action(user.file_manager_go_back):
        #    key("alt-left")
        #action(user.file_manager_go_forward):
        #    key("alt-right")
    def file_manager_open_parent():
        actions.insert('cd ..')
        actions.key('enter')
        actions.user.file_manager_refresh_title()
    def file_manager_current_path():
        path = ui.active_window().title
        path = path.replace("Administrator:  ", "").replace("Windows PowerShell: ", "")

        if path in directories_to_remap:
            path = directories_to_remap[path]

        if path in directories_to_exclude:
            path = ""
        return path

    def file_manager_open_directory(path: str):
        """opens the directory that's already visible in the view"""
        actions.insert('cd "{}"'.format(path))
        actions.key("enter")
        actions.user.file_manager_refresh_title()

    def file_manager_select_directory(path: str):
        """selects the directory"""
        actions.insert('"{}"'.format(path))

    def file_manager_new_folder(name: str):
        """Creates a new folder in a gui filemanager or inserts the command to do so for terminals"""
        actions.insert('mkdir "{}"'.format(name))

    def file_manager_open_file(path: str):
        """opens the file"""
        actions.insert(path)
        # actions.key("enter")

    def file_manager_select_file(path: str):
        """selects the file"""
        actions.insert(path)

    def file_manager_open_volume(volume: str):
        """file_manager_open_volume"""
        actions.user.file_manager_open_directory(volume)

    def terminal_list_directories():
        """Lists directories"""
        actions.insert("dir")
        actions.key("enter")

    def terminal_list_all_directories():
        actions.insert("dir /a")
        actions.key("enter")

    def terminal_change_directory(path: str):
        actions.insert("cd {}".format(path))
        if path:
          actions.key("enter")

    def terminal_change_directory_root():
        """Root of current drive"""
        actions.insert("cd /")
        actions.key("enter")

    def terminal_clear_screen():
        """Clear screen"""
        actions.insert("cls")
        actions.key("enter")

    def terminal_run_last():
        actions.key("up enter")

    def terminal_kill_all():
        actions.key("ctrl-c")
        actions.insert("y")
        actions.key("enter")
