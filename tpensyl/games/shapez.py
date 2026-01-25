from talon import Context, ctrl, actions, ui, Module
mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and app.name: shapez
"""

@mod.action_class
class ShapezActions:
    def cancel_belt_planning_mode():
        """Return true if belt planning mode was active and is now cancelled"""
        if is_in_belt_planning_mode():
            # right-click to end belt-planning mode, before releasing LMB
            ctrl.mouse_click(button=1)
            actions.user.mouse_drag_end()
            return True
        else:
            actions.user.set_hold('shift', False) # stop bulk mode
            actions.user.mouse_drag_end()
            return False

    def cancel_current():
        """Cancel bout planning or paste mode"""
        ctrl.mouse_click(button=1)
        actions.user.mouse_drag_end()

@ctx.action_class("user")
class UserActions:
    def pedal_right_down():
        actions.user.set_hold('shift', False)
        ctrl.mouse_click(button=1,down=True)

    def pedal_right_up():
        ctrl.mouse_click(button=1,up=True)

    def pedal_left_down():
        ctrl.mouse_click(button=0,down=True)

    def pedal_left_up():
        ctrl.mouse_click(button=0,up=True)

    def pedal_center_down():
        actions.user.set_hold('shift', True)
        ctrl.mouse_click(button=0,down=True)

    def pedal_center_up():
        actions.user.set_hold('shift', False)
        ctrl.mouse_click(button=0,up=True)

    def noise_trigger_pop():
        if complete_belt_planning_mode():
            return
        elif actions.user.is_held('shift'):
            ctrl.mouse_click(button=0) #is this obviated by the previous branch:
            return
        # actions.user.set_hold('shift', False)
        if actions.user.is_held('ctrl'):
            print(2)
            actions.user.mouse_drag_end()
            actions.user.set_hold('ctrl', False)
        else:
            ctrl.mouse_click(button=0)

    def noise_trigger_hiss(active):
        if active:
            if not actions.user.cancel_belt_planning_mode():
                actions.mouse_drag(1)
        else:
            ctrl.mouse_click(button=1,up=True)

    def parrot_palate():
        stopped_scrolling = stop_scrolling()
        print("stopped_scrolling=", stopped_scrolling)
        if complete_belt_planning_mode():
            # Prioritized finishing about over scrolling. Otherwise
            # scrolling is super fast because of the shift modifier
            return
        elif scroll_if_mouse_region(stopped_scrolling):
            return
        elif not stopped_scrolling:
            # start shift-dragging
            actions.user.set_hold('shift', True)
            actions.mouse_drag(0)

    def parrot_tut():
        actions.key('r')

mouse_regions = {
  # x1, x2, y1, y2
    (0, .06, 0, 1): 'a',
    (.94, 1, 0, 1): 'd',
    (0, 1, 0, .06): 's',
    (0, 1, .94, 1): 'w'
}

def is_in_belt_planning_mode():
    return (0 in ctrl.mouse_buttons_down() 
            and actions.user.is_held('shift'))

def complete_belt_planning_mode():
    is_belt_mode = is_in_belt_planning_mode()
    if is_belt_mode:
            # stop shift-dragging
            actions.mouse_release(0)
            actions.user.set_hold('shift', False)
    return is_belt_mode

# List of all buttons that were stopped.
def stop_scrolling():
    return [button for button in mouse_regions.values()
            if actions.user.set_hold(button, False)]

def scroll_if_mouse_region(stopped_scrolling):
    # If in special mouse region, hold corresponding scroll key.
    # Overlapping regions trigger multiple keys.
    mouse_pos = mouse_pos_relative_to_screen()
    buttons = [button for region, button in mouse_regions.items()
               if contains(region, *mouse_pos)]
    print("tubi", buttons, stopped_scrolling)
    if buttons != [] and buttons == stopped_scrolling:
        print("palate->stop scrolling")
        return ["stopped"]
    for button in buttons:
        actions.user.set_hold(button, True)
    return buttons

def mouse_pos_relative_to_screen():
    x, y = ctrl.mouse_pos()
    window = ui.active_window().rect
    relx = (x - window.left) / window.width
    rely = (window.top + window.height - y) / window.height  # y=0 is bottom
    return relx, rely

def contains(box, x, y):
    print(box, x, y, (box[0] <= x <= box[1]) and (box[2] <= y <= box[3]))
    return (box[0] <= x <= box[1]) and (box[2] <= y <= box[3])

print("global") 
# ui.register("app_activate", on_app_switch)