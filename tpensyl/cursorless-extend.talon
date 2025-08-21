not tag: user.cursorless 
-
# moved from core/edit/edit.talon
<user.edit_action> <user.edit_modifier>: user.edit_command(edit_action, edit_modifier)

copy head:
    edit.extend_line_start()
    edit.copy()
copy tail:
    edit.extend_line_end()
    edit.copy()

cut head:
    edit.extend_line_start()
    edit.cut()
cut tail:
    edit.extend_line_end()
    edit.cut()

chuck line: edit.delete_line()
chuck head:
    edit.extend_line_start()
    edit.delete()
chuck tail:
    edit.extend_line_end()
    edit.delete()

twin wrap this:
    text = edit.selected_text()
    user.paste("'{text}'")

quad wrap this:
    text = edit.selected_text()
    user.paste("\"{text}\"")

round wrap this:
    text = edit.selected_text()
    user.paste("({text})")

drink (this|line): edit.line_insert_up()
pour (this|line): edit.line_insert_down()


