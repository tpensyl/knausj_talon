
# * one command to clear and oleate the line properly

# ^follow$: 
#     key("ctrl:down")
#     mouse_click(0)
#     key("ctrl:up")

tracker on: tracking.control_toggle(true)
tracker off: tracking.control_toggle(false)
tracker (calibrate|calibration): tracking.calibrate()

del: key(delete)

(back|bacca): key(esc)
start menu: key(super)

m v <user.number_string>: "MV-{number_string}"

north: edit.up()
#south: edit.down()

(yap|yep): "y\n"

# junk: key(backspace)
spamma: ", "
^nope: edit.undo()
^nope nope: 
	edit.undo()
	edit.undo()
item: "* "
dot quote: "\""
junk junk: key(backspace:2)
semicolon: ";"
aero pad: "-> "

vim save:
	key(esc)
	":wq\n"

go m v <user.number_string>:
	user.switcher_focus("chrome")
	app.tab_open()
	browser.go("https://bandwidth-jira.atlassian.net/browse/MV-{number_string}")

paste plain [text]: key(ctrl-shift-v)


^boom$: mouse_click(1)

# TODO move to windows-only files
task manager: key(ctrl-shift-esc)

full screen: key(f11)

# key(keypad_enter:up): 
# 	speech.toggle()
# 	key(ctrl-shift-space)

key(f9:up): 
	speech.toggle()
	key(ctrl-shift-space)

mute discord: key(ctrl-shift-m)

mouse center: user.mouse_move_center_active_window()
mouse rest: user.mouse_rest()
mouse rest long: user.mouse_rest(5000)
read tooltip: user.mouse_rest(50000)

hold shift: key(shift:down)
hold control: key(ctrl:down)
