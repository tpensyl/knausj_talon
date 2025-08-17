mode: user.gameboy
os: windows
app.name: RuneScape Client

-

settings():
    user.hiss_scroll_denounce_time = 50

(run|walk): key(r)

take <user.number_string>: insert(number_string)
take <user.number_string> slap: 
    insert(number_string)
    sleep(30ms)
    key(enter)
say <phrase>: insert(phrase)
word <user.word>: insert(word)
slap: key(enter)
