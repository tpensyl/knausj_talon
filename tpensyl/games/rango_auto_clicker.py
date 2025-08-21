from talon import Module, ctrl, actions, cron
from typing import Union

mod = Module()

@mod.action_class
class Actions:
    def rango_auto_click(rango_target:dict, interval_ms:int=5000):
            "autoclick rango target until mouse moves"
            mouse_initial_pos = ctrl.mouse_pos()
            cron_interval = str(interval_ms) + "ms"
            rango_click_repeat(mouse_initial_pos, rango_target, cron_interval)

    def rango_auto_click_string(fuzzy_string:str, interval_ms:int=5000):
            "autoclick rango target until mouse moves"
            mouse_initial_pos = ctrl.mouse_pos()
            cron_interval = str(interval_ms) + "ms"
            rango_click_string_repeat(mouse_initial_pos, fuzzy_string, cron_interval)
              

def rango_click_repeat(mouse_initial_pos, rango_target, interval):
        if(ctrl.mouse_pos() == mouse_initial_pos):
            actions.user.rango_click_element(rango_target)
            cron.after(interval, lambda: rango_click_repeat(mouse_initial_pos, rango_target, interval))

def rango_click_string_repeat(mouse_initial_pos, rango_fuzzy_string, interval):
        if(ctrl.mouse_pos() == mouse_initial_pos):
            actions.user.rango_run_action_on_text_matched_element("clickElement", rango_fuzzy_string, False)
            cron.after(interval, lambda: rango_click_string_repeat(mouse_initial_pos, rango_fuzzy_string, interval)) 