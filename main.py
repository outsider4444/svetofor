import pygame

import SmartTrafficLight
from Pedestrian import Pedestrian, spawn_pedistrian
from Car import spawn_car, Car
from constants import WIDTH, HEIGHT, BLACK, GREEN, RED, YELLOW
from init import screen, pedestrians, crossings, cars, smart_traffic_light, traffic_light, traffic_light_p, all_sprites
from man_on_crossing import man_on_crossing

pygame.init()
# Создание флага для проверки состояния паузы
paused = False

# Устанавливаем название окна
pygame.display.set_caption("Светофор")

# Загрузка изображения для заполнения фона
background_image = pygame.image.load("images/bg.png")

# Создание машин и пешеходов
delay = 1500  # 1.5 секунды

# время, когда нужно создать следующую машину
next_circle_time = pygame.time.get_ticks() + delay

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
        screen.blit(background_image, (0, 0))

        # Спавн машин и пешеходов
        current_time = pygame.time.get_ticks()
        if current_time >= next_circle_time:
            spawn_car(cars, all_sprites)
            spawn_pedistrian(pedestrians, all_sprites)
            next_circle_time = current_time + delay

        # todo Проверка чтобы люди не шли если машина на пешеходке

        # Человек переходит дорогу - машины пропускают
        man_on_crossing(cars, pedestrians, crossings)

        # Движение машины
        for car in cars:
            # Отрисовываем машину на экране
            if 0 < car.x < WIDTH:
                car.draw(screen)
            if car.direction == "to_left":
                speed = -3
            else:
                speed = 3
            car.move(speed=speed, cars=cars, all_sprites=all_sprites)

        # отрисовка перехода
        for crossing in crossings:
            crossing.draw(screen)

        # Светофор
        # traffic_light.update()
        # traffic_light.draw(screen)

        # traffic_light_p.update()

        # Умный светофор
        smart_traffic_light.update(len(cars), len(pedestrians))
        smart_traffic_light.draw(screen)

        # Пешеходы
        for pedestrian in pedestrians:
            # Отрисовка пешехода
            if pedestrian.direction == "to_up":
                speed = -1
            else:
                speed = 1
            pedestrian.move( pedastrians=pedestrians, all_sprites=all_sprites, speed=speed)
            pedestrian.draw(screen)
        pygame.display.update()

# Выходим из игры
pygame.quit()
