from talon import Module, actions, clip
from typing import Optional
mod = Module()

@mod.action_class
class EditActions:
    def dummy_function():
        """placeholder"""
        x=3

    def go_confluence_clipboard():
        """Open the Confluence MES page whose id is on the clipboard in a new Chrome tab"""
        page_id = (clip.text() or "").strip()
        actions.user.switcher_focus("chrome")
        actions.app.tab_open()
        actions.browser.go(f"https://bandwidth-jira.atlassian.net/wiki/spaces/MES/pages/{page_id}")

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
