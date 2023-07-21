from talon import Module, actions, noise, ctrl


mod = Module()

@mod.action_class
class NoiseActions:
    # def noise_trigger_pop():
    #     """Invoked when the user does the pop noise."""
    #     print("noise_helper pop")
    #     pass

    def noise_hiss_start():
        """Invoked when the user starts hissing (potentially while speaking)"""
        pass

    def noise_hiss_stop():
        """Invoked when the user finishes hissing (potentially while speaking)"""
        pass

    def parrot_tut():
        """parrot tut sound"""
        x=1
        #print('tut unimplemented')
        pass

    def parrot_buzz():
        """parrot buzz sound"""
        pass

    def parrot_palate():
        """parrot palate sound, has some false positives with speech"""
        x=1
        #ctrl.mouse_click(0)
        #print("palate unimplemented")
        pass

    def sound_debug(name:str, power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print(name, [int(x) for x in (power, f0, f1, f2)])

# def pop_handler(active):
#     actions.user.noise_trigger_pop()

def hiss_handler(active):
    if active:
        print("hiss start")
        actions.user.noise_hiss_start()
    else:
        print("hiss stop")
        actions.user.noise_hiss_stop()

# delegating to core/noise.py
#noise.register("pop", pop_handler)
noise.register("hiss", hiss_handler)
