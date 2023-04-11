import random

import pygame

from Pedestrian import Pedestrian
from Car import Car
from constants import WIDTH, HEIGHT
from init import traffic_light, crossing, screen
from Road import Road

pygame.init()


# Устанавливаем название окна
pygame.display.set_caption("Светофор")

# Создаем объект дороги
road = Road(x=0, y=(HEIGHT - 300) // 2, width=WIDTH, height=250, strip_width=10, strip_count=20)

# Создание машину
cars_speed = random.randint(2,5)
cars = []
cars.append(Car(x=1, y=(HEIGHT // 2) + 55, radius=25, speed=0, WIDTH=WIDTH, id=1))
cars.append(Car(x=55, y=(HEIGHT // 2) + 55, radius=25, speed=0, WIDTH=WIDTH, id=2))
cars.append(Car(x=WIDTH, y=(HEIGHT // 2) - 100, radius=25, speed=0, WIDTH=WIDTH, id=3, direction="to_left"))
cars_to_right, cars_to_left = [], []
for i in range(len(cars)):
    if cars[i].y == (HEIGHT // 2) + 55:
        cars_to_right.append(cars[i])
    else:
        cars_to_left.append(cars[i])
for i in range(len(cars_to_right)):
    for j in range(len(cars_to_right)):
        if cars_to_right[i].x < cars_to_right[j].x:
            cars_to_right[i], cars_to_right[j] = cars_to_right[j], cars_to_right[i]
for i in range(len(cars_to_left)):
    for j in range(len(cars_to_left)):
        if cars_to_left[i].x < cars_to_left[j].x:
            cars_to_left[i], cars_to_left[j] = cars_to_left[j], cars_to_left[i]
cars = cars_to_right + cars_to_left
for car in cars:
    print(car.x, car.y)

# Создание пешехода
pedestrian = Pedestrian(WIDTH/2 + 85, 0, speed=0.4)

# Создаем объект для отслеживания времени
clock = pygame.time.Clock()

# Основной цикл игры
running = True
while running:
    # Ограничиваем частоту обновления кадров
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # отрисовка дороги
    road.draw(screen)

    # движение человека
    pedestrian.move(0.6)
    if crossing.y + crossing.height > pedestrian.y > crossing.y:
        for car in cars:
            # todo Была ошибка, что они наезжают на пешехода. Повторить её не смог пока что.
            if car.direction == "to_left": # Чтобы останавливаться ТОЛЬКО ЕСЛИ возле пешеходки
                pass
            if car.direction == "to_right":
                pass
    else:
        for car in cars:
            car.check_man = False

    # Отрисовываем машину на экране
    for car in cars:
        car.draw(screen)

    # Движение машины
    for car in cars:
        car.move(cars_speed)
    # отрисовка перехода
    crossing.draw(screen)

    # отрисовка светофора
    traffic_light.update()
    traffic_light.draw(screen)


    # Отрисовка пешехода
    pedestrian.draw(screen)

    pygame.display.update()
# Выходим из игры
pygame.quit()