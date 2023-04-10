import pygame

from init import traffic_light, HEIGHT, GREEN, RED, crossing, YELLOW, WIDTH


class Pedestrian:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = (255, 0, 0)  # красный цвет
        self.size = 25  # размер треугольника

    def move(self, speed):
        self.y += self.speed
        self.speed = speed
        print(self.y)
        if self.y >= crossing.y - (self.size * 2):
            if traffic_light.color == YELLOW or traffic_light.color == GREEN:
                self.speed = 0
        if self.y > HEIGHT:
            self.y = 0

    def draw(self, window):
        x1, y1 = self.x, self.y + self.size
        x2, y2 = self.x + self.size, self.y + self.size
        x3, y3 = self.x + (self.size / 2), self.y

        points = [(x1, y1), (x2, y2), (x3, y3)]
        pygame.draw.polygon(window, self.color, points)