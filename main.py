import pyautogui
import keyboard
import time
import random

while True:
    if keyboard.is_pressed("b"):
        print(pyautogui.position())
        time.sleep(1)
        break
for i in range(70, 90):
    # H
    x, y = pyautogui.position()
    pyautogui.move(xOffset=1169 - x, yOffset=249 - y)
    pyautogui.click()
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    x, y = pyautogui.position()
    pyautogui.write(str(i))

    # lambda
    x, y = pyautogui.position()
    pyautogui.move(xOffset=1172 - x, yOffset=285 - y)
    pyautogui.click()
    pyautogui.keyDown("shift")
    pyautogui.press("left", 10)
    pyautogui.keyUp("shift")
    rand = str(random.randint(0, 90))
    for i, c in enumerate(rand):
        pyautogui.write(c)
        if i == 0:
            pyautogui.press("backspace")

    # calc
    x, y = pyautogui.position()
    pyautogui.move(xOffset=1209 - x, yOffset=756 - y)
    pyautogui.click()
    time.sleep(1)
    # save
    x, y = pyautogui.position()
    pyautogui.move(xOffset=31 - x, yOffset=46 - y)
    pyautogui.click()

    # save file
    x, y = pyautogui.position()
    pyautogui.move(xOffset=65 - x, yOffset=109 - y)
    pyautogui.click()
