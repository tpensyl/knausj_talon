mode: user.gameboy
tag: user.game_media
-
^volume up$: key(volup:2)
^volume up <number_small>$: key('volup:{number_small}')
^volume down$: key(voldown:2)
^volume down <number_small>$: key('voldown:{number_small}')
#set volume <number>: user.media_set_volume(number)
^volume mute$: key(mute)