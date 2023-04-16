import random

import pygame

from constants import RED, BLACK, GREEN, HEIGHT, WIDTH, YELLOW
from init import traffic_light, crossings, screen, cars, cars_to_right, cars_to_left


class Car:
    def __init__(self, x, y, radius, speed, id, direction="to_right"):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = 0  # начальная скорость по оси X
        self.max_speed_x = 10  # максимальная скорость по оси X
        self.acceleration = 1  # константа ускорения
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
            for crossing in crossings:
                if self.direction == "to_right":
                    # Машина рядом с пешеходкой
                    if crossing.id == 0:
                        if crossing.x - (self.radius + 3) <= self.x <= crossing.x + self.radius:
                            if traffic_light.color == RED or (
                                    traffic_light.color == YELLOW and traffic_light.new_color == "red"):
                                self.speed = 0
                    if crossing.id == 1:
                        if self.x > crossings[0].x + crossings[0].width and self.x <= crossing.x:
                            self.speed = speed
                    # Проезд на желтый
                    if self.x + self.radius > crossing.x and self.x <= crossing.x + crossing.width:
                        self.speed = speed
                    # if crossing.id == 1:
                    # if self.x + self.radius > crossing.x and self.x <= crossing.x + crossing.width:
                    #     self.speed = speed
                if self.direction == "to_left":
                    if crossing.id == 1:
                        # Машина рядом с пешеходкой
                        if crossing.x + crossing.width + (self.radius + 3) >= self.x >= (
                                crossing.x + crossing.width) - self.radius:
                            if traffic_light.color == RED or (
                                    traffic_light.color == YELLOW and traffic_light.new_color == "red"):
                                self.speed = 0
                    if crossing.id == 0:
                        if self.x > crossings[1].x + crossings[1].width and self.x <= crossing.x:
                            self.speed = speed
                    # Проезд на желтый
                    if self.x - self.radius < crossing.x + crossing.width and self.x >= crossing.x:
                        self.speed = speed
        self.x += self.speed

    # def accelerate(self,):
    #     if self.speed < self.max_speed_x:
    #         self.speed += self.acceleration

    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius)
        # Показ координат
        font = pygame.font.Font(None, 20)
        # Вывод координат в машинке
        text_coor = font.render(f"{self.x + self.radius}, {self.y}", True, (0, 0, 0))
        # Вывод id машинки
        text = font.render(f"{self.id}", True, (255, 255, 255))
        # screen.blit(text, (self.x - text.get_width() // 2, self.y - text.get_height() // 2))
        # screen.blit(text_coor, (self.x - text.get_width() // 2, (self.y - text.get_height() // 2) - 35))


id = 1
direction = "to_right"


# Спавн машинок, едущих направо
def spawn_car_to_right():
    global id
    global cars_to_right
    if len(cars_to_right) < 13:
        direction = "to_right"
        speed = 4
        y = (HEIGHT // 2) + 50
        x = -50
        car = Car(x=x, y=y, radius=25, speed=speed, id=id, direction=direction)
        cars_to_right.append(car)
        cars.append(car)
        id += 1

# Спавн машинок, едущих налево
def spawn_car_to_left():
    global id
    global cars_to_left
    if len(cars_to_left) < 8:
        direction = "to_left"
        speed = -4
        y = (HEIGHT // 2) - 80
        x = WIDTH
        car = Car(x=x, y=y, radius=25, speed=speed, id=id, direction=direction)
        cars_to_left.append(car)
        cars.append(car)
        id += 1


# Удаление машинок
def delete_car():
    global cars_to_right
    global cars_to_left
    global cars
    for i in range(len(cars_to_right)):
        if cars_to_right[i].x >= WIDTH:
            cars_to_right.pop(i)
            cars.pop(i)
            break
    for j in range(len(cars_to_left)):
        if cars[j].x <= 0:
            cars_to_left.pop(j)
            cars.pop(j)
            break
