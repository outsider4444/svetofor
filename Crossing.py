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
        font = pygame.font.Font(None, 20)
        texet_e = font.render(f"({self.x + self.width}, {self.y})", True, (255, 255, 255))
        text_s = font.render(f"({self.x}, {self.y})", True, (255, 255, 255))
        # Показ координат
        screen.blit(texet_e, ((self.x - texet_e.get_width() // 2) + self.width, (self.y - texet_e.get_height() // 2) - 15))
        screen.blit(text_s, ((self.x - text_s.get_width() // 2), (self.y - text_s.get_height() // 2) - 15))
        screen.blit(self.surface, (self.x, self.y))

    def return_x(self):
        return self.x