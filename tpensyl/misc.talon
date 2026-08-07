
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
(back|bacca) (back|bacca): 
	key(esc)
	sleep(20ms)
	key(esc)
	
start menu: key(super)

m v <user.number_string>: "MV-{number_string}"

north: edit.up()
#south: edit.down()

(yap|yep): "y\n"

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
unicode trademark: "™"
unicode cents: "¢"
unicode pencil: "✎"
unicode (check | checkmark): "✅"
unicode [red] x: "❌"

(vim|vem) save:
	key(esc)
	":wq\n"

go m v <user.number_string>:
	user.switcher_focus("chrome")
	app.tab_open()
	browser.go("https://bandwidth-jira.atlassian.net/browse/MV-{number_string}")
confluence that: user.go_confluence_clipboard()
go here:
    edit.copy()
    #url = edit.selected_text()
	user.switcher_focus("chrome")
	sleep(100ms)
	app.tab_open()
	sleep(50ms)
	user.address_focus()
	edit.paste()
	key(enter)
	#browser.go(url)

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

dedent that:
    user.remove_indentation()

# address common misrecognition with ordinals (6th, 7th)
<user.number> slash: "{number}/"