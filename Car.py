import random

import pygame

from constants import RED, BLACK, GREEN, HEIGHT, WIDTH, YELLOW
from init import traffic_light, crossings, screen, cars, cars_to_right, cars_to_left


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, speed, id, direction="to_right"):
        super().__init__()
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

    def car_checker(self):
        if self.direction == "to_left":
            if self.x + self.radius < WIDTH:
                if self.x - (self.radius + 10) > 0:
                    color = screen.get_at((self.x - (self.radius + 10), self.y))
                    if color == BLACK:
                        self.check_car = True
                    else:
                        self.check_car = False
        elif self.direction == "to_right":
            # Проверка на наличие машины рядом
            if 0 < self.x + (self.radius + 10) < WIDTH:
                color = screen.get_at((self.x + (self.radius + 10), self.y))
                if color == BLACK:
                    self.check_car = True
                else:
                    self.check_car = False

    def move(self, speed, cars, all_sprites):
        self.speed = speed
        self.car_checker()
        # На переходе человек или рядом машинка
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
                        if crossings[0].x + crossings[0].width < self.x <= crossing.x:
                            self.speed = speed
                    # Проезд на желтый
                    if self.x + self.radius > crossing.x and self.x <= crossing.x + crossing.width:
                        self.speed = speed
                if self.direction == "to_left":
                    if crossing.id == 1:
                        # Машина рядом с пешеходкой
                        if crossing.x + crossing.width + (self.radius + 3) >= self.x >= (
                                crossing.x + crossing.width) - self.radius:
                            if traffic_light.color == RED or (
                                    traffic_light.color == YELLOW and traffic_light.new_color == "red"):
                                self.speed = 0
                    if crossing.id == 0:
                        if crossings[1].x + crossings[1].width < self.x <= crossing.x:
                            self.speed = speed
                    # Проезд на желтый
                    if self.x - self.radius < crossing.x + crossing.width and self.x >= crossing.x:
                        self.speed = speed

        self.remove_if_off_screen(cars, all_sprites=all_sprites)
        self.x += self.speed

    def remove_if_off_screen(self, cars, all_sprites):
        if (self.direction == "to_left" and self.x + self.radius < 0) or (
                self.direction == "to_right" and self.x - self.radius > WIDTH):
            for i in range(len(cars)):
                if self.id == cars[i].id:
                    cars.pop(i)
                    break
            self.kill()
            self.remove(all_sprites)
            del self

    def draw(self, screen):
        # pygame.draw.circle(screen, RED, (int(self.x) + self.radius + 10, int(self.y)), 1)
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius)
        font = pygame.font.Font(None, 20)
        text_coor = font.render(f"{self.x + self.radius}, {self.y}", True, (0, 0, 0))  # Вывод координат в машинке
        text = font.render(f"{self.id}", True, (255, 255, 255))  # Вывод id машинки
        # screen.blit(text, (self.x - text.get_width() // 2, self.y - text.get_height() // 2))
        # screen.blit(text_coor, (self.x - text.get_width() // 2, (self.y - text.get_height() // 2) - 35))


id = 0
direction = "to_right"


def spawn_car(cars, all_sprites):
    global id
    global direction
    if len(cars) < 70:
        if direction == "to_left":
            speed = -4
            y = (HEIGHT // 2) - 75
            x = WIDTH
            car = Car(x=x, y=y, radius=25, speed=speed, id=id, direction=direction)
            cars.append(car)
            id += 1
            direction = "to_right"
            all_sprites.add(car)
        if direction == "to_right":
            speed = 4
            y = (HEIGHT // 2) + 50
            x = -50
            car = Car(x=x, y=y, radius=25, speed=speed, id=id, direction=direction)
            cars.append(car)
            id += 1
            direction = "to_left"
            all_sprites.add(car)
