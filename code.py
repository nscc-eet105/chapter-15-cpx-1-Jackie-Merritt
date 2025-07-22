from adafruit_circuitplayground import cp
# from dataclasses import dataclass
import time
# Jackie-Merritt_Chp14-CPX1_7/14/2025


class Region:
    def __init__(self, color, leds):
        self.__color = color
        self.__leds = leds
        self.__tone = x[leds]

    def set_color(self, color):
        self.__color = color

    def set_leds(self, leds):
        self.__leds = leds

    def set_tone(self, tone):
        self.__tone = tone

    def get_color(self):
        print(f'{self.__color}')

    def get_leds(self):
        print(f'{self.__leds}')

    def get_tone(self):
        print(f'{self.__tone}')

    def all_on(self):
        for pixel in self.__leds:
            cp.pixels[pixel] = self.__color

    def all_off(self):
        for pixel in self.__leds:
            cp.pixels[pixel] = (0, 0, 0)

    def play_tone(self, duration):
        cp.play_tone(self.__tone, duration)

x = {'yellow': (255, 255, 0), 'blue': (0, 0, 255), 'red': (255, 0 , 0), 'green': (0, 255, 0), (5, 6, 7): 252, (2, 3, 4): 209, (7, 8, 9): 310, (0, 1, 2): 415}

yellow = Region((255, 255, 0), (5, 6, 7))
blue = Region((0, 0, 255), (2, 3, 4))
red = Region((255, 0, 0), (7, 8, 9))
green = Region((0, 255, 0), (0, 1, 2))

while True:
    yellow.all_on()
    yellow.play_tone(.8)
    time.sleep(.2)
    yellow.all_off()
    # time.sleep(.2)
    green.all_on()
    green.play_tone(.8)
    time.sleep(.2)
    green.all_off()
    # time.sleep(.2)
    blue.all_on()
    blue.play_tone(.8)
    time.sleep(.2)
    blue.all_off()
    # time.sleep(.2)
    red.all_on()
    red.play_tone(.8)
    time.sleep(.2)
    red.all_off()
    # time.sleep(.2)
