from talon import Module, ui, actions, scope

mod = Module()
mod.mode("gameboy", desc="Limited command mode intended for games")

game_list = [
    "Satisfactory", 
    "Age of Empires: Definitive Edition", 
    "FTLGame.exe", 
    "Sokobond.exe",
    "Talos"
]

def on_app_switch(app):
    #print(f"App [{app.name}] triggered.")
    modes = scope.get("mode")
    if modes is None:
        return
    # if "sleep" in modes:
    #     return
        
    if app.name in game_list:
        if "user.gameboy" not in modes:
            actions.mode.disable("command")
            actions.mode.enable("user.gameboy")
            print(f"App [{app.name}] triggered gameboy mode.")
    else:
        if "user.gameboy" in modes:
            actions.mode.enable("command")
            actions.mode.disable("user.gameboy")
            actions.mode.disable("sleep")
            actions.mode.disable("dictation")
            print(f"App [{app.name}] triggered command mode.")

ui.register("app_activate", on_app_switch)

