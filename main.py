import pygame

from Pedestrian import Pedestrian
from Car import Car, spawn_car, delete_car
from constants import WIDTH, HEIGHT
from init import traffic_light, crossing, screen, cars
from Road import Road

pygame.init()
# Создание флага для проверки состояния паузы
paused = False

# Устанавливаем название окна
pygame.display.set_caption("Светофор")

# Создаем объект дороги
road = Road(x=0, y=(HEIGHT - 300) // 2, width=WIDTH, height=250, strip_width=10, strip_count=20)

# Создание машину
delay = 1500  # 1 секунды

# время, когда нужно создать следующий круг
next_circle_time = pygame.time.get_ticks() + delay

# cars.append(Car(x=1, y=(HEIGHT // 2) + 55, radius=25, speed=0, WIDTH=WIDTH, id=1))
# cars.append(Car(x=WIDTH, y=(HEIGHT // 2) - 100, radius=25, speed=0, WIDTH=WIDTH, id=3, direction="to_left"))

car = Car(x=1, y=(HEIGHT // 2) + 55, radius=25, speed=0, WIDTH=WIDTH, id=0)
cars.append(car)

# Создание пешехода
pedestrian = Pedestrian(WIDTH / 2 + 85, 50, speed=0)

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
            # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused  # Изменение значения флага при нажатии на пробел
    if not paused:
        # отрисовка дороги
        road.draw(screen)

        # Спавн и удаление машин
        current_time = pygame.time.get_ticks()
        if current_time >= next_circle_time:
            spawn_car(cars)
            next_circle_time = current_time + delay
        delete_car(cars)

        # движение человека
        pedestrian.move(0.6)

        # если человек на светофоре
        if pedestrian.check_crossing:
            # если машина возле пешеходки
            for car in cars:
                if crossing.x - car.radius <= car.x <= crossing.x + car.radius:
                    car.check_man = True
                else:
                    car.check_man = False
        else:
            for car in cars:
                car.check_man = False

        # Отрисовываем машину на экране
        for car in cars:
            if car.x > 0:
                car.draw(screen)

        # Движение машины
        for car in cars:
            car.move(4)
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
