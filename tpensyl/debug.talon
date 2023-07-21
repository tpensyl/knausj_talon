-
# I have mapped the Olympus RS31H foot pedal to these virtual keys.
# see https://liannaee.blogspot.com/2023/03/olympus-rs31h-hardware-with-talon-voice.html


# Left Peddle
key(f16): 
    print("f13")

# Center Pedal
key(f17):
    print("f14")

# Right Pedal
key(f18):
    print("f15")

# Top Puddle
key(f19): 
    print("f16")
test: print("test")
gamepad(dpad_up):           print("dpad_up")
gamepad(dpad_down):         print("dpad_down")
gamepad(dpad_left):         print("dpad_left")
gamepad(dpad_right):        print("dpad_right")

gamepad(north):             print("north/Y")
gamepad(west):              print("west/X")
gamepad(east):              print("east/B")
gamepad(south):             print("south/A")

gamepad(select):            print("select/view")
gamepad(start):             print("start/menu")

gamepad(l1):                print("l1/Left bumper")
gamepad(r1):                print("r1/Right bumper")

gamepad(l2:change):         print("l2/Left trigger {value}")
gamepad(r2:change):         print("r2/Right trigger {value}")

gamepad(l3):                print("l3/Left stick click")
gamepad(r3):                print("r3/Right stick click")

gamepad(left_xy):           print("left_xy: {x}, {y}")
gamepad(right_xy):          print("right_xy: {x}, {y}")