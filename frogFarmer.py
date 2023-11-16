import pyautogui
import sys
import time

heightOffset = float(sys.argv[1])


screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

print(screenWidth, screenHeight)
print(currentMouseX, currentMouseY)
time.sleep(15)



while True:
    pyautogui.moveTo(screenWidth/2, (screenHeight/2) + heightOffset)
    pyautogui.click()
    time.sleep(15)
    pyautogui.move(0, 45)
    pyautogui.click()
    time.sleep(15)
    pyautogui.move(0, 45)
    pyautogui.click()
    time.sleep(15)
    pyautogui.move(0, 45)
    pyautogui.click()
    time.sleep(15)