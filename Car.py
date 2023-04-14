import random

import pygame

from constants import RED, BLACK, GREEN, HEIGHT, WIDTH, YELLOW
from init import traffic_light, crossing, screen, cars


class Car:
    def __init__(self, x, y, radius, speed, id, direction="to_right"):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.direction = direction
        self.check_man = False
        self.check_car = False
        self.id = id
        self.spawn_time = pygame.time.get_ticks()

    def car_checker(self):
        if self.direction == "to_left":
            if self.x + self.radius < WIDTH:
                if self.x - (self.radius + 10) > 0:
                    color = screen.get_at((self.x - (self.radius + 10), self.y))
                    if color == (0, 0, 0):
                        self.check_car = True
                    else:
                        self.check_car = False
        elif self.direction == "to_right":
            # Проверка на наличие машины рядом
            if self.x - self.radius > 0:
                if self.x + (self.radius + 10) < WIDTH:
                    color = screen.get_at((self.x + (self.radius + 10), self.y))
                    if color == (0, 0, 0):
                        self.check_car = True
                    else:
                        self.check_car = False

    def move(self, speed):
        self.speed = speed
        self.car_checker()
        # На пешеходке человек или рядом машинка
        if self.check_man or self.check_car:
            self.speed = 0
        else:
            if self.direction == "to_right":
                # Машина рядом с пешеходкой
                if crossing.x - (self.radius + 3) <= self.x <= crossing.x + self.radius:
                    if traffic_light.color == RED or (traffic_light.color == YELLOW and traffic_light.new_color == "red"):
                        self.speed = 0
                # Проезд на желтый
                if self.x + self.radius > crossing.x and self.x <= crossing.x + crossing.width:
                    self.speed = speed
            if self.direction == "to_left":
                # Машина рядом с пешеходкой
                if crossing.x + crossing.width + (self.radius + 3) >= self.x >= (crossing.x + crossing.width) - self.radius:
                    if traffic_light.color == RED or (traffic_light.color == YELLOW and traffic_light.new_color == "red"):
                        self.speed = 0
                # Проезд на желтый
                if not self.check_man:
                    if self.x - self.radius < crossing.x + crossing.width and self.x >= crossing.x:
                        self.speed = speed
        self.x += self.speed


    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius)
        # Показ координат
        font = pygame.font.Font(None, 20)
        # Вывод координат в машинке
        text_coor = font.render(f"{self.x + self.radius}, {self.y}", True, (0, 0, 0))
        # Вывод id машинки
        text = font.render(f"{self.id}", True, (255, 255, 255))
        screen.blit(text, (self.x - text.get_width() // 2, self.y - text.get_height() // 2))
        # screen.blit(text_coor, (self.x - text.get_width() // 2, (self.y - text.get_height() // 2) - 35))


id = 1
direction = "to_right"
def spawn_car(cars):
    global id
    global direction

    if len(cars) < 20:
        if direction == "to_left":
            speed = -4
            y = (HEIGHT // 2) - 100
            x = WIDTH
            car = Car(x=x, y=y, radius=25, speed=speed, id=id, direction=direction)
            cars.append(car)
            id += 1
            direction = "to_right"
        if direction == "to_right":
            speed = 4
            y = (HEIGHT // 2) + 55
            x = -50
            car = Car(x=x, y=y, radius=25, speed=speed, id=id, direction=direction)
            cars.append(car)
            id += 1
            direction = "to_left"

def delete_car(cars):
    global id
    for i in range(len(cars)):
        if (cars[i].direction == "to_right" and cars[i].x >= WIDTH) or (cars[i].direction == "to_left" and cars[i].x <= 0):
            cars.pop(i)
            break
