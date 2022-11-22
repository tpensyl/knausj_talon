from talon import Context, actions, Module
import time
ctx = Context()
ctx.matches = r"""
win.title: /DOSBox-X.*/
"""
mod = Module()

def multikey(k1,k2):
    actions.key(k1+':down')
    actions.key(k2+':down')
    actions.key(k1+':up')
    actions.key(k2+':up')

@mod.action_class
class UserActions:
    def quick_save():
        """Quick save"""
        multikey('f11', 's')
        #Enable: "no remark when saving state"
        #time.sleep(.1)
        #actions.insert("talon")
        #actions.key('enter')

    def quick_load():
        """Quick load"""
        multikey('f11', 'l')
        
    def previous_slot():
        """Previous slot"""
        multikey('f11', ',')

    def next_slot():
        """Next slot"""
        multikey('f11', '.')

    def toggle_full_screen():
        """Next slot"""
        multikey('f11', 'f')
