mode: user.gameboy
and win.title: /.*melonDS.*/
-

settings():
    # minimum silence time (in seconds) before speech is cut off, default 0.3
    speech.timeout = .2 
    user.default_long_press_ms = .128
    user.default_long_wait_ms = .150
	
up:     user.press_wait('up')
down:   user.press_wait('down')
left:   user.press_wait('left')
right:  user.press_wait('right')
bump left:   user.press_wait('l')
bump right:  user.press_wait('r')
#start:  user.long_press('w')
select: user.press_wait('q')
(pop | bang):    user.press_wait('a')    
    #user.long_press('a', .032)
    #sleep(278ms)
back:   user.press_wait('b')
(speed | turbo): user.long_press('t', .032)
(menu|start):	user.long_press('x', .032)
