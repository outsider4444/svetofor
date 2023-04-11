import pygame

from constants import RED, BLACK, GREEN
from init import traffic_light, crossing, screen


class Car:
    def __init__(self, x, y, radius, speed, WIDTH, id, direction="to_right"):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.WIDTH = WIDTH
        self.direction = direction
        self.check_man = False
        self.check_car = False,
        self.id = id

    def move(self, speed):
        self.speed = speed
        if self.check_man == True:
            self.speed = 0

        if self.check_car == True:
            self.speed = 0
        if self.direction == "to_right":

            # Проверка на наличие машины рядом
            if self.x + (self.radius+10) < self.WIDTH:
                color = screen.get_at((self.x + (self.radius+10), self.y))
                if color == (0, 0, 0):
                    print("Рядом с машиной есть другая машина!")
                    self.speed = 0
                else:
                    self.speed = speed

            if self.x >= crossing.x - self.radius and crossing.x + crossing.width > self.x <= self.WIDTH:
                if traffic_light.color != GREEN:
                    self.speed = 0
            self.x += self.speed
            if self.x > self.WIDTH:
                self.x = 0

        elif self.direction == "to_left":
            if self.x <= crossing.x + crossing.width + self.radius and self.x >= crossing.x:
                if traffic_light.color != GREEN:
                    self.speed = 0
            self.x -= self.speed
            if self.x < 0:
                self.x = self.WIDTH


    def draw(self, surface):
        pygame.draw.circle(surface, BLACK, (int(self.x), int(self.y)), self.radius)