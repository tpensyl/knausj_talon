app: sublime
-

tag(): user.tabs
tag(): user.generic_unix_shell
tag(): user.git

todo: "TODO "
todo <user.text>: "TODO {text}"
done: "DONE"

[go] line <user.number_string>:
	key(ctrl-g)
	"{number_string}"
	key(enter)

file open: key(ctrl-o)

### adoated from 2shea/knausj_talon
# Sublime Tools
sidebar: key(ctrl-0)
console: key(ctrl-`)
[command] pallet: key(ctrl-shift-p)

# Layout and View
(column | row) one: key(alt-ctrl-1)
column two: key(alt-ctrl-2)
column three: key(alt-ctrl-3)
row two: key(shift-alt-ctrl-2)
row three: key(shift-alt-ctrl-3)
grid: key(alt-ctrl-5)

# Code Navigation

jump paren: key(ctrl-m)
jump: key(ctrl-alt-f)
(jump back | jack): key(ctrl-alt-b)
jump (up | start): key(ctrl-up)
jump (down | end): key(ctrl-down)

# Find & Replace
replace: key(ctrl-h)
(subl | sublime) find: key(ctrl-f)
[(subl | sublime)] find all: key(ctrl-shift–f)
expression: key(alt-r)
case insensitive: key(alt-c)
whole word: key(alt-w)

# Text Selection
move line up: key(ctrl-shift-up)
move line down: key(ctrl-shift-down)
cursor push: key(ctrl-shift-l)
cursor pop:
  key(ctrl-shift-l)
  key(ctrl-left)
cursor undo: key(ctrl-u)
zoom out: key(ctrl--)
zoom in: key(ctrl-=)

all word: key(ctrl-ctrl-g)
(select | cell) scope: key(shift-ctrl-space)
(select | cell) (bracket | paren): key(shift-ctrl-m)
(select | cell) indent: key(shift-ctrl-j)
bounce [right]: key(ctrl-alt-shift-right)
(bound | bounce back): key(ctrl-alt-shift-left)

(upper | uppercase | upcase):
  key(ctrl-k)
  key(ctrl-u)
(lower | lowercase | downcase):
  key(ctrl-k)
  key(ctrl-l)

# Editing
comment: key(ctrl-/)
snipline: key(ctrl-shift-k)
dup line: key(ctrl-shift-d)
up slap: key(ctrl-shift-enter)
(scrap | delete) word: key(alt-backspace)
(scrap | delete) (begin | start | pop): key(ctrl-backspace)

#TODO deprecated
action(edit.indent_less):
       key(ctrl-[)

action(edit.indent_more):
       key(ctrl-])

shove:
  edit.indent_more()
tug:
  edit.indent_less()