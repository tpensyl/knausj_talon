from talon import Module, ui, actions, scope

mod = Module()
mod.mode("gameboy", desc="Limited command mode intended for games")

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
    "Quest.exe"
]


ahk_script_dir = "C:\\games\\ahk-scripts\\"
ahk_script_map = {
    "Talos": "talos-pad.ahk",
    "Unofficial source port for Blake Stone classic series": "bstone-joy.ahk" 
}
ahk_kill_switch = "f24"

def on_app_switch(app):
    # print(f"App [{app.name}] triggered.")
    modes = scope.get("mode")
    if modes is None:
        return
    # if "sleep" in modes:
    #     return
        
    if app.name in game_list:
        if "user.gameboy" not in modes:
            actions.mode.disable("command")
            actions.mode.enable("user.gameboy")
            print(f"App [{app.name}] triggered gameboy mode: win.title=[{actions.win.title()}]")

            if app.name in ahk_script_map:
                ahk_script = ahk_script_dir + ahk_script_map[app.name]
                print(f"Running AHK script: {ahk_script}")
                actions.user.system_command_nb(ahk_script)
    else:
        if "user.gameboy" in modes:
            actions.mode.enable("command")
            actions.mode.disable("user.gameboy")

            actions.key(ahk_kill_switch)
            # Sometimes the key doesn't get through during the context switch?  
            actions.sleep("100ms")
            actions.key(ahk_kill_switch)

            print(f"App [{app.name}] triggered command mode.")



ui.register("app_activate", on_app_switch)

