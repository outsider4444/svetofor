import pygame

import init
from constants import RED
from init import traffic_light, HEIGHT, crossing, WIDTH


class Pedestrian:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = (255, 0, 0)  # красный цвет
        self.size = 25  # размер треугольника
        self.check_crossing = False
        self.direction = "to_down"
        self.check_car = False

    def move(self, speed=None):
        self.speed = speed
        # НЕ красный
        if traffic_light.color != RED:
            # Чуть выше чем верхняя граница перехода
            if crossing.y - self.size <= self.y <= crossing.y:
                self.speed = 0
                self.check_crossing = False
            if self.y > crossing.y + crossing.height:
                self.check_crossing = False
        # Красный
        elif traffic_light.color == RED:
            if crossing.y <= self.y <= crossing.y + crossing.height:
                self.check_crossing = True
            if self.y > crossing.y + crossing.height:
                self.check_crossing = False
        # Проверка на машину на пешеходке
        if self.check_car == True:
            self.speed = 0

        self.y += self.speed
        if self.y > 600:
            self.y = 50

    def draw(self, window):
        x1, y1 = self.x, self.y + self.size
        x2, y2 = self.x + self.size, self.y + self.size
        x3, y3 = self.x + (self.size / 2), self.y

        points = [(x1, y1), (x2, y2), (x3, y3)]
        pygame.draw.polygon(window, self.color, points)
