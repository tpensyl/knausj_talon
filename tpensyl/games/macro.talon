mode: user.gameboy
and win.title: /.*VisualBoyAdvance.*/
-

cycle: user.start_cycle_up_down('1000ms')
fast: user.start_cycle_up_down('150ms')

run:
    user.long_press('l')
    user.long_press('down',.1)
    user.long_press('right',.1)
    user.long_press('l',.1)
    sleep(32ms)
    user.long_press('l',.1)
