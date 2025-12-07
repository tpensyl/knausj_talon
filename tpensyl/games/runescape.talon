mode: user.gameboy
os: windows
app.name: RuneScape Client

-

settings():
    user.hiss_scroll_debounce_time = 50
    speech.timeout = 0.1

tag(): user.game_generic_keys

{user.search_engine} hunt <user.text>$:
    user.search_with_search_engine(search_engine, user.text)

(run|walk): key(r)
(surge|search|sprint): key(alt-1)
jump back: key(alt-2)
defend: key(alt-3)
eat: key(alt-4)
charge: key(alt-5)
pray: key(alt-o)
loot: key(alt-l)

pad: key(space)
comma: key(,)
question: key(?)
bang: key(!)

(go home): key(shift-1)
(alk|alky|alchemy|gold|alk that|alk it|gold): key(shift-2)

go (stuff|inventory|backpack): 
    key(alt-b)
    sleep(5ms)
    user.mouse_move_window_relative(.92, .75)
stuff: key(alt-b)
minimap: user.mouse_move_window_relative(.92, .15)

(equipment|gear): key(alt-e)
(stats|skills): key(alt-s)
go (stats|skills):
    keyb(alt-s)
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
say <phrase>: insert(phrase)
word <user.word>: insert(word)
slap: key(enter)

drag: user.mouse_drag(0)

(and die|and I): key(keypad_multiply)