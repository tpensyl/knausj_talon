from talon import Module, actions, noise


mod = Module()

@mod.action_class
class ParrotNoiseActions:
    def whistle_start(ts:float, power:float, f0:float, f1:float, f2:float):
        "whistle start stub"
        print('whistle stark stub')
        x = 1

    def whistle_stop(ts:float, power:float, f0:float, f1:float, f2:float):
        "whistle stop stub"
        x = 1

    def whistle_repeat(ts:float, power:float, f0:float, f1:float, f2:float):
        "whistle repeat stub"
        x = 1