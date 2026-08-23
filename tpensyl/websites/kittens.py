from talon import Context, Module, ctrl, actions, cron
ctx = Context()
ctx.matches = r"""
win.title: /Kittens Game.*/
"""

mod = Module()
@mod.action_class
class NoiseActions:
    def kitten_click(i: int): 
        """use ctrl+click=?x to reduce clicks - depends on config""" 
        actions.key("ctrl:down")
        actions.user.game_click(0, i//25, "25ms")
        actions.key("ctrl:up")
        actions.user.game_click(0, i%25, "25ms")

    def kitten_test():
        """test scratch"""
        trade_leviathans_20()

    def kitten_end_game_loop():
        """trade and max chronospheres, cryochambers. appropriate for end game exponential resources"""
        kitten_end_game_loop_recursive_1()

    def kitten_end_game_loop_b():
        """trade and max chronospheres, cryochambers. appropriate for end game exponential resources"""
        kitten_end_game_loop_recursive_2()

def kitten_end_game_loop_recursive_1():
    build_workshop()
    build_all("chronosphere")
    switch_tab("science")
    build("tachyon theory")
    actions.user.game_click(0, times = 5,  wait = "10ms")
    #build("void space")
    #build("paradox theory")
    switch_tab("time")
    build("chronocontrol")
    build("cryochamber") #1, maxed
    build("workshop")
    build("chronoforge")
    actions.user.game_click(0, times = 15,  wait = "10ms")
    #build("flux condensator")
    #build("chronosurge")
    switch_tab("time")
    actions.user.rango_snap_scroll_text("Combust TC", "top")
    cron.after("1500ms", kitten_end_game_loop_recursive_2)

def kitten_end_game_loop_recursive_2():
    build_all("temporal battery")
    build_all("fix cryochamber") # sets up mouse
    for _ in range(8):
        combust_max()
        actions.user.game_click(0, wait="100ms", modifier="shift")
    actions.sleep("100ms")
    #repeat
    trade_leviathans_20()
    switch_tab("bonfire")
    build_all("chronosphere")
    switch_tab("time")
    #build_all("reset")
    #cron.after("2s", kitten_end_game_loop_recursive_1)

def switch_tab(tab: str):
    actions.user.rango_click_text(tab)
    actions.sleep("350ms")

def build(building: str):
    actions.sleep("20ms")
    actions.user.rango_click_text(building)
    actions.sleep("30ms")

def build_many(building: str):
    actions.sleep("20ms")
    actions.user.rango_click_text(building, "ctrl")
    actions.sleep("250ms")
    actions.key("enter")

def build_all(building: str):
    actions.sleep("20ms")
    actions.user.rango_click_text(building, "shift")
    actions.sleep("250ms")
    actions.key("enter")

def trade_leviathans_20():
    """50% leviathan trade"""
    build("trade")
    actions.sleep("100ms")
    actions.user.rango_run_action_on_text_matched_element("focusElement", "feed elders")
    actions.user.multi_press("tab", 3, "0ms", "20ms")
    actions.key("enter")

def combust_max():
    """max combust size"""
    actions.user.rango_run_action_on_text_matched_element("focusElement", "combust")
    actions.user.multi_press("tab", 4, "0ms", "25ms")
    actions.key("enter")
    actions.sleep("250ms")

def build_workshop():
    """build workshop assuming no science - regular method selects the tab"""
    actions.user.rango_run_action_on_text_matched_element("focusElement", "hut")
    actions.key("tab enter")

@ctx.action_class("user")
class UserActions:
    def pedal_right_down():
        #ctrl.mouse_click(0)
        #actions.user.rango_run_action_on_text_matched_element("clickElement", "leviathon", False)
        actions.key("ctrl:down")
        ctrl.mouse_click(0)
        actions.key("ctrl:up")

    def pedal_center_down():
        actions.user.rango_run_action_on_text_matched_element("clickElement", "zebra", False)
        #actions.user.mouse_auto_click(250)

    def pedal_top_down():
        actions.key("shift:down")
        ctrl.mouse_click(0)
        actions.key("shift:up")
        actions.sleep("250ms")
        actions.key("enter")

    def parrot_tut():
        actions.key("ctrl:down")
        ctrl.mouse_click(0)
        actions.key("ctrl:up")



