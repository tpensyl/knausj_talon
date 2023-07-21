from talon import Context, actions, ctrl
ctx = Context()

@ctx.action_class('user')
class UserActions:
    def noise_trigger_pop():
        print("pop-click_default")
        #ctrl.mouse_click(button=1, up=True)
        actions.user.stop_mouse_move()
        actions.user.slow_click()

    def noise_hiss_start():
        ctrl.mouse_click(button=0, down=True)

    def noise_hiss_stop():
        ctrl.mouse_click(button=0, up=True)
