from talon import Module, ui, actions, scope

mod = Module()
mod.mode("gameboy", desc="Limited command mode intended for games")

mod.mode("gameboy_sleep", desc="For commands to be disabled when talking other people")

# Trigger gameboy mode when app.name is in this list
game_list = [
    "FactoryGame", 
    "Age of Empires: Definitive Edition", 
    "FTLGame.exe", 
    "Sokobond.exe",
    "Talos",
    "DSPGAME.exe",
    "DOSBox DOS Emulator",
    "Unofficial source port for Blake Stone classic series",
    "Adobe Flash Player 29.0 r0",
    "Space Engineers",
    "RCT.EXE",
    "Main executable for OpenRCT2",
    "http://www.scummvm.org/",
    "Crystal Caves HD.exe",
    "Quest.exe",
    "RuneScape Client",
    "shapez",
    "Borderlands 2"
]


ahk_script_dir = "C:\\games\\ahk-scripts\\"
ahk_script_map = {
    "Talos": "talos-pad.ahk",
    "Unofficial source port for Blake Stone classic series": "bstone-joy.ahk" 
}
ahk_kill_switch = "f24"

def on_app_switch(app):
    global nongame_modes
    # bprint(f"App [{app.name}] triggered.")
    modes = scope.get("mode")
    if modes is None:
        return
    # if "sleep" in modes:
    #     return
    
    if app.name in game_list:
        if "user.gameboy" not in modes:
            actions.mode.disable("command")
            actions.mode.disable("sleep")
            actions.mode.enable("user.gameboy")
            print(f"App [{app.name}] triggered gameboy mode: win.title=[{actions.win.title()}]")

            if "sleep" in modes:
                actions.mode.enable("user.gameboy_sleep")

            if app.name in ahk_script_map:
                ahk_script = ahk_script_dir + ahk_script_map[app.name]
                print(f"Running AHK script: {ahk_script}")
                actions.user.system_command_nb(ahk_script)
    else:
        if "user.gameboy" in modes:
            print("switching from gameboy mode to regular")
            actions.user.set_hold('shift', False)
            actions.user.set_hold('ctrl', False)
            actions.mode.enable("sleep" if "user.gameboy_sleep" in modes else "command")
            actions.mode.disable("user.gameboy")
            actions.mode.disable("user.gameboy_sleep")

            actions.key(ahk_kill_switch)
            # Sometimes the key doesn't get through during the context switch?  
            actions.sleep("100ms")
            actions.key(ahk_kill_switch)

            print(f"App [{app.name}] triggered command mode.")



ui.register("app_activate", on_app_switch)

