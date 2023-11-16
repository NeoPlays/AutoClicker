from pynput import mouse
import time
import sys

def on_click(x, y, button, pressed):
    global gotAllPositions
    if(not pressed):
        if(button == mouse.Button.left and not gotAllPositions):
            print("Left Click")
            posArray.append((x, y))
            print("Added Position: " + str(x) + ", " + str(y))
        elif(button == mouse.Button.right):
            print("Right Click")
            gotAllPositions = True

posArray = []
gotAllPositions = False
clicker = mouse.Controller()

listener = mouse.Listener(on_click=on_click)
listener.start()

while True:
    if(gotAllPositions):
        for pos in posArray:
            clicker.position = pos
            time.sleep(0.25)
            clicker.click(mouse.Button.left, 1)
            time.sleep(int(sys.argv[1]))
