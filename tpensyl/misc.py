import shutil
import subprocess
from talon import Module, actions, clip
from typing import Optional
mod = Module()

VS_CODE_CLI_FALLBACKS = [
    "/usr/local/bin/code",
    "/opt/homebrew/bin/code",
    "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code",
]

def copy_selection_text():
    """Copy the current selection and return it, falling back to the clipboard when nothing is selected"""
    try:
        with clip.capture() as captured:
            actions.edit.copy()
        text = captured.text()
    except clip.NoChange:
        text = clip.text()
    return (text or "").strip()

@mod.action_class
class EditActions:
    def dummy_function():
        """placeholder"""
        x=3

    def copy_selection_for_go_here():
        """Copy the selection, strip a stray surrounding paren, and leave it on the clipboard to paste"""
        text = copy_selection_text()
        if text.startswith("("):
            text = text[1:]
        if text.endswith(")"):
            text = text[:-1]
        clip.set_text(text.strip())

    def go_jira_mv(ticket_number: str):
        """Open the MV-<ticket_number> Jira issue in Chrome"""
        # See go_confluence_clipboard for why we use `open` instead of browser.go.
        url = f"https://bandwidth-jira.atlassian.net/browse/MV-{ticket_number}"
        subprocess.Popen(["open", "-a", "Google Chrome", url])

    def go_confluence_clipboard():
        """Copy the selection, then open the Confluence MES page with that id in a new Chrome tab"""
        page_id = copy_selection_text()
        url = f"https://bandwidth-jira.atlassian.net/wiki/spaces/MES/pages/{page_id}"
        # Hand the URL straight to Chrome via `open` rather than the browser.go path below.
        # switcher_focus() is async, so when this runs from a non-browser app, browser.go
        # fires before Chrome's browser context is active and throws NotImplementedError
        # ("Action 'browser.go' exists but the Module method is empty ...").
        # `open` targets Chrome regardless of focus, opens a new tab, and raises the window.
        subprocess.Popen(["open", "-a", "Google Chrome", url])
        # actions.user.switcher_focus("chrome")
        # actions.app.tab_open()
        # actions.browser.go(url)

    def code_open_clipboard():
        """Copy the selection, then open that path in the existing VS Code window (`code -r`)"""
        target = copy_selection_text()
        code_cli = shutil.which("code") or next(
            (path for path in VS_CODE_CLI_FALLBACKS if shutil.which(path)), None
        )
        if not code_cli:
            actions.app.notify("VS Code `code` CLI not found")
            return
        try:
            subprocess.run([code_cli, "-r", target], check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as error:
            actions.app.notify(f"code failed: {error.stderr.strip() or error}")

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
