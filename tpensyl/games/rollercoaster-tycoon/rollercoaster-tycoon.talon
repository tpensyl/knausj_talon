mode: user.gameboy
app.name: /RCT.EXE/
app.name: /.*OpenRCT2/
-

<phrase>$: skip()

settings():
    speech.timeout = .13

insert password: "farts"

open research: key(d)
open finance: key(f)
open guest: key(g)
(bill|build) (right|riot|ride): key(f5)
terraform: key(f1)

mark (right|ride) [height]: "("r
mark land [height]: key(8)
mark ride [height]: key(9)
mark path [height]: key(0)

view underground: key(1)
view underwater: key(2)
hide (rides|ride): key(3)
hide (trees|scenery): key(4)
hide supports: key(5)
hide people: key(6)
hide grid: key(7)
hide land top: key(h)
hide land side: key(v)

rotate screen: "["
zoom in: key(pgdn)
zoom out: key(pgup)

turn: key(z)
turn two: key(z:2)
turn three: key(z:3)
