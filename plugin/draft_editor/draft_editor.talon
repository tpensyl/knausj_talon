user.draft_editor_running: True
not tag: user.draft_editor_app_focused
-

draft (this|that): user.draft_editor_open()

draft all:
  edit.select_all()
  user.draft_editor_open()

draft line:
  edit.select_line()
  user.draft_editor_open()

draft up <number>:
  edit.select_line()
  key(shift-up)
  repeat(number - 1)
  user.draft_editor_open()

draft down <number>:
  key(home:2)
  key(shift-end)
  key(shift-down)
  repeat(number - 1)
  user.draft_editor_open()

draft around <number>:
  key(up)
  repeat(number - 1)
  key(home:2)
  key(shift-end)
  key(shift-down)
  repeat(number)
  repeat(number - 1)
  user.draft_editor_open()

draft top:
  edit.extend_file_start()
  user.draft_editor_open()

draft bottom:
  edit.extend_file_end()
  user.draft_editor_open()

# draft submit:
#   user.draft_editor_paste_last()
