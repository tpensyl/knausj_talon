# Compound of action(select, clear, copy, cut, paste, etc.) and modifier(word,
# line, etc.) commands for editing text.
# eg: "select line", "clear all"
#tpensyl - moving to exclude from cursorless contexts
# <user.edit_action> <user.edit_modifier>: user.edit_command(edit_action, edit_modifier)

# Zoom
zoom in: edit.zoom_in()
zoom out: edit.zoom_out()
zoom reset: edit.zoom_reset()

# Searching
find it: edit.find()
next one: edit.find_next()

# Navigation

# The reason for these spoken forms is that "page up" and "page down" are globally defined as keys.
scroll up: edit.page_up()
scroll down: edit.page_down()

# go left, go left left down, go 5 left 2 down
# go word left, go 2 words right
go <user.navigation_step>+: user.perform_navigation_steps(navigation_step_list)

# go line start | head: edit.line_start()
go line end | tail: edit.line_end()

go way left:
    edit.line_start()
    edit.line_start()
go way right: edit.line_end()
go way up: edit.file_start()
go way down: edit.file_end()

go top: edit.file_start()
go bottom: edit.file_end()

go page up: edit.page_up()
go page down: edit.page_down()

# Selecting

# select left: edit.extend_left()
# select right: edit.extend_right()
# select up: edit.extend_line_up()
# select down: edit.extend_line_down()

# select word left: edit.extend_word_left()
# select word right: edit.extend_word_right()

# select way left: edit.extend_line_start()
# select way right: edit.extend_line_end()
# select way up: edit.extend_file_start()
# select way down: edit.extend_file_end()

# Indentation
(indent [more] | shove): edit.indent_more()

(indent less | out dent | tug): edit.indent_less()

# Copy
copy that: edit.copy()

# Cut
cut that: edit.cut()

# Paste
((pace | paste) (that | it) | pit slap): edit.paste()
(pace | paste) enter:
    edit.paste()
    key(enter)
paste match: edit.paste_match_style()

# Duplication

# Insert new line
new line above: edit.line_insert_up()
new line below | slap: edit.line_insert_down()

# Insert padding with optional symbols
(padding): user.insert_between(" ", " ")
(padding) <user.symbol_key>+:
    insert(" ")
    user.insert_many(symbol_key_list)
    insert(" ")

# Undo/redo
undo that: edit.undo()
redo that: edit.redo()

# Save
file save: edit.save()
file save all: edit.save_all()

[go] line mid: user.line_middle()
