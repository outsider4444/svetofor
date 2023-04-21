import pygame

import init
from constants import RED
from init import traffic_light, HEIGHT, crossings, WIDTH


class Pedestrian(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, id, direction="to_down"):
        super().__init__()
        self.check_man = False
        self.x = x
        self.y = y
        self.speed = speed
        self.id = id
        self.color = (255, 0, 0)  # красный цвет
        self.size = 25  # размер треугольника
        self.check_crossing = False
        self.direction = direction
        self.ready = False
        self.check_car = False

    def man_checker(self):
        if self.direction == "to_down":
            if self.y + self.size + 10 < HEIGHT and self.y > 0:
                color = init.screen.get_at((int(self.x) + self.size // 2, self.y + (self.size + 10)))
                if color == RED:
                    self.check_man = True
                else:
                    self.check_man = False
        elif self.direction == "to_up":
            if self.y - 10 > 0 and self.y + self.size < HEIGHT:
                color = init.screen.get_at((int(self.x) + self.size // 2, self.y - 10))
                if color == RED:
                    self.check_man = True
                else:
                    self.check_man = False

    def move(self, pedastrians, all_sprites, speed=None):
        self.speed = speed
        self.man_checker()
        self.remove_if_off_screen(pedastrians, all_sprites)
        # Проверка на машину или человека рядом
        if self.check_man or self.check_car:
            self.speed = 0
        else:
            # сверху вниз
            for crossing in crossings:
                if self.direction == "to_down":
                    # НЕ красный
                    if traffic_light.color != RED:
                        # Чуть выше чем верхняя граница перехода
                        if (crossing.y - self.size) - 3 <= self.y <= crossing.y:
                            self.speed = 0
                            self.check_crossing = False
                        if self.y > crossing.y + crossing.height:
                            self.check_crossing = False
                    # Красный
                    elif traffic_light.color == RED:
                        # Чуть ниже чем нижняя граница перехода
                        if crossing.y <= self.y <= crossing.y + crossing.height:
                            self.check_crossing = True
                        if self.y > crossing.y + crossing.height:
                            self.check_crossing = False
                # снизу вверх
                elif self.direction == "to_up":
                    if traffic_light.color != RED:
                        # Чуть выше чем верхняя граница перехода
                        if (crossing.y + crossing.height) + 3 >= self.y >= crossing.y + crossing.height:
                            self.speed = 0
                            self.check_crossing = False
                        if self.y < crossing.y:
                            self.check_crossing = False
                    # Красный
                    elif traffic_light.color == RED:
                        if crossing.y + crossing.height >= self.y >= crossing.y:
                            self.check_crossing = True
                        if self.y < crossing.y:
                            self.check_crossing = False
                self.y += self.speed

    def remove_if_off_screen(self, pedastrians, all_sprites):
        if (self.direction == "to_up" and self.y - self.size < 0) or (
                self.direction == "to_down" and self.y > HEIGHT):
            for i in range(len(pedastrians)):
                if self.id == pedastrians[i].id:
                    pedastrians.pop(i)
                    break
            self.kill()
            self.remove(all_sprites)
            del self

    def draw(self, window):
        x1, y1 = self.x, self.y + self.size
        x2, y2 = self.x + self.size, self.y + self.size
        x3, y3 = self.x + (self.size / 2), self.y

        points = [(x1, y1), (x2, y2), (x3, y3)]
        pygame.draw.polygon(window, self.color, points)
        # pygame.draw.circle(window, RED, (int(self.x) + self.size // 2, int(self.y) - 15), 1)


direction = "to_down"
id = 0


def spawn_pedistrian(pedistrians, all_sprites):
    global direction, id
    if len(pedistrians) < 18:
        if direction == "to_down":
            speed = 1
            y = 0
            x = (WIDTH / 2) - 200
            pedistrian = Pedestrian(x, y, speed=speed, direction="to_down", id=id)
            pedistrians.append(pedistrian)
            all_sprites.add(pedistrian)
            direction = "to_up"
            id += 1
        if direction == "to_up":
            speed = -1
            y = 720
            x = (WIDTH / 2) + 175
            pedistrian = Pedestrian(x, y, speed=speed, direction="to_up", id=id)
            pedistrians.append(pedistrian)
            all_sprites.add(pedistrian)
            direction = "to_down"
            id += 1
