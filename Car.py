import random

import pygame

from constants import RED, BLACK, GREEN, HEIGHT, WIDTH, YELLOW
from init import traffic_light, crossing, screen, cars


class Car:
    def __init__(self, x, y, radius, speed, WIDTH, id, direction="to_right"):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.WIDTH = WIDTH
        self.direction = direction
        self.check_man = False
        self.check_car = False
        self.id = id
        self.spawn_time = pygame.time.get_ticks()

    def move(self, speed):
        self.speed = speed
        # Проверка на наличие машины рядом
        if self.x - self.radius > 0:
            if self.x + (self.radius + 10) < self.WIDTH:
                color = screen.get_at((self.x + (self.radius + 10), self.y))
                if color == (0, 0, 0):
                    self.check_car = True
                else:
                    self.check_car = False
        if self.direction == "to_right":
            # На пешеходке человек или рядом машинка
            if self.check_man or self.check_car:
                self.speed = 0
            else:
                # Машина рядом с пешеходкой
                if crossing.x - (self.radius + 1) <= self.x <= crossing.x + self.radius:
                    if traffic_light.color == RED or (traffic_light.color == YELLOW and traffic_light.new_color != "green"):
                        self.speed = 0
                if self.x + self.radius >= crossing.x and self.x <= crossing.x + crossing.width:
                    if traffic_light.new_color == "green":
                        print("Я ТИПА МОГ БЫ ПРОЕХАТЬ", self.id, traffic_light.new_color)
                        self.speed = speed
            self.x += self.speed
        # if self.direction == "to_right":
        #     if self.x >= crossing.x - self.radius and crossing.x + crossing.width > self.x <= self.WIDTH:
        #         if traffic_light.color != GREEN and self.x < crossing.x:
        #             self.speed = 0
        # elif self.direction == "to_left":
        #     if self.x <= crossing.x + crossing.width + self.radius and self.x >= crossing.x:
        #         if traffic_light.color != GREEN:
        #             self.speed = 0
        #     self.x -= self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius)
        # Показ координат
        font = pygame.font.Font(None, 20)
        # Вывод координат в машинке
        # text = font.render(f"{self.x + self.radius}, {self.y}", True, (255, 255, 255))
        # Вывод id машинки
        text = font.render(f"{self.id}", True, (255, 255, 255))
        screen.blit(text, (self.x - text.get_width() // 2, self.y - text.get_height() // 2))


id = 1


def spawn_car(cars):
    global id
    direction = "to_right"
    if len(cars) < 20:
        car = Car(x=-50, y=(HEIGHT // 2) + 55, radius=25, speed=0, WIDTH=WIDTH, id=id, direction=direction)
        cars.append(car)
        id += 1


def delete_car(cars):
    global id
    for i in range(len(cars)):
        if cars[i].x >= WIDTH:
            cars.pop(i)
            break
