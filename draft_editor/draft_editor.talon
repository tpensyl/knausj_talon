user.draft_editor_running: True
not tag: user.draft_editor_app_focused
-

draft this:
	user.draft_editor_open()

draft all:
	edit.select_all()
	user.draft_editor_open()

draft line:
	edit.select_line()
	user.draft_editor_open()

draft up <number_small>:
	edit.select_line()
	key(shift-up)
	repeat(number_small - 1)
	user.draft_editor_open()

draft down <number_small>:
	key(home:2)
	key(shift-end)
	key(shift-down)
	repeat(number_small - 1)
	user.draft_editor_open()