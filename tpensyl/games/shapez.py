from talon import Context, ctrl, actions, ui
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and app.name: shapez
"""

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
        if actions.user.is_held('shift'):
            ctrl.mouse_click(button=0)
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
            is_in_belt_planning_mode = (
                    0 in ctrl.mouse_buttons_down() 
                and actions.user.is_held('shift')
            ) 
            if is_in_belt_planning_mode:
                # right-click to end belt-planning mode, before releasing LMB
                ctrl.mouse_click(button=1)
                actions.user.mouse_drag_end()
            else:
                actions.user.set_hold('shift', False) # stop bulk mode
                actions.user.mouse_drag_end()
                actions.mouse_drag(1)
        else:
            ctrl.mouse_click(button=1,up=True)

    def parrot_palate():
        stopped_scrolling = stop_scrolling()
        print("stopped_scrolling=", stopped_scrolling)
        if 0 in ctrl.mouse_buttons_down():
            # stop shift-dragging
            actions.mouse_release(0)
            actions.user.set_hold('shift', False)
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