^gameboy mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.disable("command")
	mode.enable("user.gameboy")

^gameboy mode off$:
	mode.disable("user.gameboy")
	mode.enable("command")
	
^add gameboy mode$:
	mode.enable("user.gameboy")