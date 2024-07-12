from selenium import webdriver
from PIL import ImageGrab
import pyautogui as gui
import numpy as np

gui.useImageNotFoundException()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://elgoog.im/dinosaur-game/")
driver.maximize_window()


while True:
    img = np.array(ImageGrab.grab(bbox=(150, 580, 400, 630), include_layered_windows=True))
    if [83, 83, 83] in img or [172, 172, 172] in img:
        gui.press('space')
