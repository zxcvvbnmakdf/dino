import numpy
from PIL import ImageGrab,ImageOps
import pyautogui
import time


class DinoBot:
    def __init__(self,replay_button,x1,y1,x2,y2):
        self.replay_button = replay_button
        self.x1 =x1
        self.y1 =y1
        self.x2 =x2
        self.y2 =y2
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
        box =(1260,284 , 1315 ,315)
        image = ImageGrab.grab(box)
        gray_scale_image = ImageOps.grayscale(image)
        pixels_array = numpy.array(gray_scale_image.getcolors())
        print(pixels_array.sum())
        return pixels_array.sum()

    def start(self):
        self.restart_game()
        while True:
            if self.grab_image() != 1952:
               self.jump()


def main():
    bot = DinoBot(replay_button=(1430, 280), x1=1260, y1=284, x2=1315,y2=315)
    bot.start()


if __name__ == "__main__":
    main()