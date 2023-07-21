from talon import Context, Module, actions, ctrl, actions
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
app.name: Age of Empires: Definitive Edition
"""
mod = Module()

control_group_list = "zero one two three four five six seven eight nine".split()
control_group_map = {word: str(i) for i, word in enumerate(control_group_list)}

mod.list("control_group", desc="List of assignable control groups in AOE1")
ctx.lists["self.control_group"] = control_group_map


repeat_num_list = "two three four five six seven eight nine".split()
repeat_num_map = {word: str(i + 2) for i, word in enumerate(repeat_num_list)}

mod.list("repeat_num", desc="List of numbers used for repeating")
ctx.lists["self.repeat_num"] = repeat_num_map  

@mod.capture(rule="{user.repeat_num}")
def repeat_num(m) -> int:
    return int(m.repeat_num)

# One button mouse interface
@ctx.action_class('user')
class UserActions:
    def noise_pop():
        ctrl.mouse_click(0)

    def noise_hiss_start():
        # Right-click drag to scroll viewport
        #ctrl.mouse_click(0, down=True)
        ctrl.mouse_click(1) # Deselect
        ctrl.mouse_click(button=1, down=True)

    def noise_hiss_stop():
        ctrl.mouse_click(button=1, up=True)
        #ctrl.mouse_click(0, up=True)


    def parrot_palate():
        ctrl.mouse_click(1) # Deselect
        ctrl.mouse_click(0)

    def parrot_tut():
        buttons_held_down = list(ctrl.mouse_buttons_down())
        if buttons_held_down:
            for button in buttons_held_down:
                ctrl.mouse_click(button=button, up=True)
            return
        else:
            ctrl.mouse_click(button=0, down=True)
