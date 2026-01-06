mode: user.gameboy
and not mode: user.gameboy_sleep
os: windows
app.name: RuneScape Client

-
^go to sleep$: 
    # set up the stack in case we wake up outside of gameboy mode
    mode.enable("command")
    mode.disable("user.gameboy")
    # turn off captions
    speech.disable()
    mode.enable("user.gameboy")
    mode.disable("sleep")
    mode.enable("user.gameboy_sleep")

tag(): user.game_generic_keys
say <phrase>: insert(phrase)

#<phrase>: skip()

settings():
    user.hiss_scroll_debounce_time = 40
    key_wait = 32
    speech.timeout = 0.1

^(back|bacca)$: key(esc)
touch: mouse_click(0)

{user.search_engine} hunt <user.text>$:
    user.search_with_search_engine(search_engine, user.text)

^(run|walk)$: key(r)
(surge|search|sprint): key(alt-1)
jump back: key(alt-2)
defend: key(alt-3)
(chump|chomp): key(alt-4)
charge: key(alt-5)
(and die|and I): key(alt-6)
# (and die|and I): key(keypad_multiply)
pray: key(alt-o)
loot: key(alt-l)

pad: key(space)
comma: key(,)
question: key(?)
bang: key(!)

(go home): key(shift-1)
(alk|alky|alchemy|gold|alk that|alk it|gold): key(shift-2)
soil box: key(shift-4)

go (stuff|inventory|backpack): 
    key(alt-b)
    sleep(5ms)
    user.mouse_move_window_relative(.92, .75)
stuff: key(alt-b)
[go] minimap: user.mouse_move_window_relative(.92, .15)

(equipment|gear): key(alt-e)
(stats|skills): key(alt-s)
go (stats|skills):
    key(alt-s)
    sleep(5ms)
    user.mouse_move_window_relative(.92, .75)
magic: key(alt-m)
pick prayer: key(alt-p)
notes: key(alt-n)
challenge: key(f3)

^<number_small>$: key("{number_small}")
(pick) <user.number_string>: insert(number_string)
take <user.number_string>:
    insert(number_string)
    sleep(30ms)
    key(enter)
word <user.word>: insert(word)
slap: key(enter)

drag: user.mouse_drag(0)