from talon import Context, actions, ctrl
ctx = Context()

@ctx.action_class('user')
class UserActions:
    def noise_trigger_pop():
        print("pop-click_actions.py")
        #ctrl.mouse_click(button=1, up=True)
        # if actions.user.interrupt_mouse_rest():
        #     return
        actions.user.stop_mouse_move()
        actions.user.slow_click()

    # def noise_hiss_start():
    #     ctrl.mouse_click(button=0, down=True)
    #     return
 
    # def noise_hiss_stop():
    #     ctrl.mouse_click(button=0, up=True)
    #     return
