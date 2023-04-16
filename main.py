import pygame

from Pedestrian import Pedestrian
from Car import Car, delete_car, spawn_car_to_right, spawn_car_to_left
from constants import WIDTH, HEIGHT, BLACK, GREEN, RED
from init import traffic_light, screen, cars, pedestrians, crossings
from man_on_crossing import man_on_crossing

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
# pedestrian1 = Pedestrian((WIDTH / 2) - 200, 0, speed=1, direction="to_down")
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
        pygame.draw.circle(screen, RED, (WIDTH-5, (HEIGHT // 2)-80), 1)
        pygame.draw.circle(screen, RED, (8, (HEIGHT // 2)+50), 1)

        # todo Спавн и удаление машин
        current_time = pygame.time.get_ticks()
        check_car_to_spawn_right = screen.get_at((8, (HEIGHT // 2) + 50))
        check_car_to_spawn_left = screen.get_at((WIDTH-5, (HEIGHT // 2) - 80))
        if current_time >= next_circle_time:
            if check_car_to_spawn_right != (0, 0, 0):
                spawn_car_to_right()
            if check_car_to_spawn_left != (0, 0, 0):
                spawn_car_to_left()
            next_circle_time = current_time + delay
        delete_car()

        # todo Проверка чтобы люди не шли если машина на пешеходке

        # Человек переходит дорогу - машины пропускают
        man_on_crossing(cars, pedestrians, crossings)

        # Движение машины
        for car in cars:
            # Отрисовываем машину на экране
            if -1 < car.x < WIDTH + 5:
                car.draw(screen)
            if car.direction == "to_left":
                speed = -3
            else:
                speed = 3
            # car.accelerate()  # ускоряем круг
            car.move(speed=speed)

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
