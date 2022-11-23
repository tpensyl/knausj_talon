mode: user.gameboy
#TODO how to make reuseable, but optional?
win.title: /.*DOSBox.*ZORK.*/
-

# -1 because we are repeating, so the initial command counts as one
<user.ordinals>: core.repeat_command(ordinals-1)
ocho: core.repeat_command(8-1)
<number_small>: core.repeat_command(number_small-1)
<number_small> times: core.repeat_command(number_small-1)
(repeat that|twice): core.repeat_command(1)
#repeat that <number_small> [times]: core.repeat_command(number_small)
