mode: user.gameboy
tag: user.game_generic_keys
-

<user.letter>: key(letter)
<user.special_key>: key(special_key)
<user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")
# for key combos consisting only of modifiers, eg. `press shift`.
<user.modifiers>$: key(modifiers)
(up|north): key(up)
down: key(down)
left: key(left)
right: key(right)
slap: key(enter)
back: key(esc)