import pygame

from Pedestrian import Pedestrian
from Car import spawn_car, Car, all_sprites
from constants import WIDTH, HEIGHT, BLACK, GREEN, RED
from init import traffic_light, screen, pedestrians, crossings, cars
from man_on_crossing import man_on_crossing

from TrafficTest import TrafficLight

pygame.init()
# Создание флага для проверки состояния паузы
paused = False

# Устанавливаем название окна
pygame.display.set_caption("Светофор")

# Создаем объект дороги
# Загрузка изображения для заполнения фона
background_image = pygame.image.load("images/Background.png")

# Создание машину
delay = 1000  # 1 секунды

# время, когда нужно создать следующую машину
next_circle_time = pygame.time.get_ticks() + delay

# Пешеходы
pedestrian1 = Pedestrian((WIDTH / 2) - 200, 0, speed=1, direction="to_down")
pedestrian2 = Pedestrian(WIDTH / 2 + 175, 650, speed=-1, direction="to_up")
pedestrians.append(
    pedestrian1
)
pedestrians.append(
    pedestrian2
)

# Создаем объект для отслеживания времени
clock = pygame.time.Clock()

# Основной цикл игры
running = True
while running:
    # Ограничиваем частоту обновления кадров
    clock.tick(30)
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
        traffic_light_test.change_color("red", 5)
        traffic_light_test.draw()
        # Спавн и удаление машин
        current_time = pygame.time.get_ticks()
        if current_time >= next_circle_time:
            spawn_car(cars)
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
            car.move(speed=speed, cars=cars)

        # отрисовка перехода
        for crossing in crossings:
            crossing.draw(screen)

        # отрисовка светофора
        traffic_light.update()
        traffic_light.draw(screen)

        for pedestrian in pedestrians:
            # Отрисовка пешехода
            if pedestrian.direction == "to_up":
                speed = -1
            else:
                speed = 1
            pedestrian.move(speed)
            pedestrian.draw(screen)
        pygame.display.update()

# Выходим из игры
pygame.quit()
