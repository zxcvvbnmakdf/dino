import numpy
from PIL import ImageGrab,ImageOps
import pyautogui
import time


class DinoBot:
    def __init__(self,replay_button):
        self.replay_button = replay_button

    def restart_game(self):
        pyautogui.click(self.replay_button)

    def clicker_test(self):
        for i in range(100):
            pyautogui.click(self.replay_button)

    def jump(self):
        pyautogui.keyDown("space")
        time.sleep(0.05)
        pyautogui.keyUp("space")

    def grab_image(self):
        box =(1260,284 , 1330,315)
        image = ImageGrab.grab(box)
        gray_scale_image = ImageOps.grayscale(image)
        pixels_array = numpy.array(gray_scale_image.getcolors())
        print(pixels_array.sum())
        return pixels_array.sum()

    def start(self):
        self.restart_game()
        while True:
            if self.grab_image() != 2417:
               self.jump()


def main():
    bot = DinoBot((1430, 280))
    bot.start()


if __name__ == "__main__":
    main()