from talon import Context, Module, actions, ctrl
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
app.exe: FTLGame.exe
"""
mod = Module()

ftl_crew_list = "one two three four five six seven eight".split()
ftl_crew_map = {word: 'f' + str(i + 1) for i, word in enumerate(ftl_crew_list)}

mod.list("ftl_crew", desc="FTL crew numbers")
ctx.lists["self.ftl_crew"] = ftl_crew_map

@ctx.action_class('user')
class UserActions:
    def noise_pop():
        ctrl.mouse_click(0)

    def noise_hiss_start():
        ctrl.mouse_click(button=0, down=True)

    def noise_hiss_stop():
        ctrl.mouse_click(button=0, up=True)

    def parrot_palate():
        actions.key("space")

    def parrot_tut():
        ctrl.mouse_click(1)
        #actions.user.toggle_drag(0)

@mod.action_class
class FTLActions:
    def target_gun(key: str):
        """Select weapon and click e.g. to target"""
        actions.key(key)
        actions.sleep("15ms")
        actions.mouse_click(0)
