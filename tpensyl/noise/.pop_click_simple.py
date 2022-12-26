from talon import noise, ctrl
import time

def game_click(active):
        ctrl.mouse_click(button=0, down=True)
        time.sleep(.016) #16ms
        ctrl.mouse_click(button=0, up=True)

noise.register("pop", game_click)