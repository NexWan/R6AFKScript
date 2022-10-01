import time
import keyboard
import pyautogui as pg
import random as ran

file = open("config.txt","r")
start = file.readline().splitlines()
end = file.readline().splitlines()

print(start)
print(end)

while True:
    if keyboard.is_pressed(start):
        while True:
            x = ran.randint(0, 1000)
            y = ran.randint(0, 750)
            pg.moveTo(x, y, 0.5)
            time.sleep(2)
            if keyboard.is_pressed(end):
                quit()