from talon import Context, Module, actions, ctrl
ctx = Context()
ctx.matches = r"""
app.name: Age of Empires: Definitive Edition
"""
mod = Module()

control_group_list = "one two three four five six seven eight nine".split()
control_group_map = {word: str(i + 1) for i, word in enumerate(control_group_list)}

mod.list("control_group", desc="List of assignable control groups in AOE1")
ctx.lists["self.control_group"] = control_group_map


repeat_num_list = "two three four five six seven eight nine".split()
repeat_num_map = {word: str(i + 2) for i, word in enumerate(repeat_num_list)}

mod.list("repeat_num", desc="List of numbers used for repeating")
ctx.lists["self.repeat_num"] = repeat_num_map  

# One button mouse interface
@ctx.action_class('user')
class UserActions:
    def noise_pop():
        ctrl.mouse_click(0)

    def noise_hiss_start():
        ctrl.mouse_click(1)
        ctrl.mouse_click(button=0, down=True)

    def noise_hiss_stop():
        ctrl.mouse_click(button=0, up=True)
