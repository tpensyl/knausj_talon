mode: command
mode: dictation
-
^dictation mode$: user.dictation_mode()
^command mode$:
    user.command_mode()
    mode.disable("user.gameboy")
^mixed mode$:
    mode.disable("sleep")
    mode.enable("dictation")
    mode.enable("command")

^gameboy mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.disable("command")
    mode.enable("user.gameboy")
    speech.disable()
