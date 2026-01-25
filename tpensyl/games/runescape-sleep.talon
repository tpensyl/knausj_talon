mode: user.gameboy
mode: user.gameboy_sleep
os: windows
app.name: RuneScape Client

-

settings():
    user.hiss_scroll_debounce_time = 40

^wake up$: 
    speech.enable()
    mode.disable("user.gameboy_sleep")

# one: key(1)
# (five|next): key(5)
loot: key(alt-l)
(surge|search): key(alt-1)
charge: key(alt-5)
bones: key(shift-5)

# <phrase>: skip()

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
(teleport|magicp): key(alt-m)

runescape hunt <user.text>$:
    user.search_with_search_engine('https://runescape.wiki/w/Special:Search?search=%s', user.text)