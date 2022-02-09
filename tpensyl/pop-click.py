from talon import noise, ctrl

def on_pop(active: bool):
    ctrl.mouse_click(button=0)


#noise.register("hiss", on_pop)
noise.register("pop", on_pop)
