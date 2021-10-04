from PIL import Image
from PIL import ImageGrab
from pyautogui import press
import pyautogui
import time
import numpy as np

# snapshot = ImageGrab.grab()
# save_path = "C:\\Users\\luisr\\pic.png"
# snapshot.save(save_path)

def detect_color(img, x, y):
    gs_im = img.convert('L')
    g = gs_im.getpixel((y, x))
    return round(g / 255.0)

def get_environment(img):
    color = detect_color(img, 100, 100)
    if color == (255, 255, 255):
        return True
    else:
        return False

def jump():
    # pyautogui.press('up')
    pyautogui.keyDown('up')
    pyautogui.keyUp('up')

def crouch():
    pyautogui.press('down')

def detect_obstacle(img):
    for i in range(200, 650, 5):
        color = detect_color(img, 645, i)
        if color == (0):
            print("JUMP")
            jump()
            break
            # print(color)

def start_game():
    running = True
    index = 1
    while running: 
        snapshot = ImageGrab.grab()
        # snapshot = Image.open("C:\\Users\\luisr\\15.png")
        # print(np.array(snapshot).shape)
        # is_day = get_environment(snapshot)
        detect_obstacle(snapshot)
        # save_path = f"C:\\Users\\luisr\\{index}.png"
        # snapshot.save(save_path)
        # save_path = f"C:\\Users\\luisr\\{index}.png"
        # snapshot.save(save_path)
        # index = index + 1
        # running = False


start_game()