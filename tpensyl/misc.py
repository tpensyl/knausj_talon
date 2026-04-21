from talon import Module, actions
from typing import Optional
mod = Module()

@mod.action_class
class EditActions:
    def dummy_function():
        """placeholder"""
        x=3 

    def remove_indentation():
        """Remove lowest common level of indentation of the currently selected text"""
        original = actions.edit.selected_text() or ""
        new = remove_indentation(original)
        actions.clip.set_text(new)
        actions.edit.paste()
    
def remove_indentation(text):
    """Remove lowest common level of the indentation, e.g. for pasting code in slack with minimal indentation"""
    lines = text.splitlines()
    minimum_indentation = min([len(line) - len(line.lstrip()) for line in lines])
    stripped_lines = [line[minimum_indentation:] for line in lines]
    return '\n'.join(stripped_lines)
