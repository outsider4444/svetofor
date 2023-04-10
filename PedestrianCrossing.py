import pygame


class PedestrianCrossing:
    width = 0
    x = 0

    def __init__(self, x, y, width=100, height=250, border=2):
        self.x = x
        self.y = y-100
        self.width = width
        self.height = height
        self.border = border

        # Создаем поверхность для квадрата
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        # Задаем цвет квадрата и его прозрачность
        self.surface.fill((255, 255, 255, 128))
        # Рисуем красную границу квадрата
        pygame.draw.rect(self.surface, (255, 0, 0), self.surface.get_rect(), self.border)

    def draw(self, screen):
        # Отображаем квадрат на экране
        screen.blit(self.surface, (self.x, self.y))

    def return_x(self):
        return self.x