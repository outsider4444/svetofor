import pygame


class PedestrianCrossing:
    width = 0
    x = 0

    def __init__(self, x, y, width=100, height=200, border=2, _id=0, direction="vertical"):
        self.id = _id
        self.x = x
        self.y = y-100
        self.width = width
        self.height = height
        self.border = border
        self.direction = direction
        # Создаем поверхность для квадрата
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        if self.direction == "horizontal":
            self.surface = pygame.Surface((self.height, self.width), pygame.SRCALPHA)
        # Задаем цвет квадрата и его прозрачность
        self.surface.fill((255, 255, 255, 128))
        # Рисуем красную границу квадрата
        pygame.draw.rect(self.surface, (255, 0, 0, 255), self.surface.get_rect(), self.border)

    def draw(self, screen):
        # Отображаем квадрат на экране
        font = pygame.font.Font(None, 20)
        texet_e = font.render(f"({self.x + self.width}, {self.y})", True, (255, 255, 255))
        text_s = font.render(f"({self.x}, {self.y})", True, (255, 255, 255))
        text_id = font.render(f"{self.id}", True, (0, 0, 0))
        # Показ координат
        # screen.blit(text_s, ((self.x - text_s.get_width() // 2), (self.y - text_s.get_height() // 2) - 15))
        # screen.blit(texet_e, ((self.x - texet_e.get_width() // 2) + self.width, (self.y - texet_e.get_height() // 2) - 15))
        # screen.blit(text_id, ((self.x + text_s.get_width() // 2), (self.y + texet_e.get_height())))
        # screen.blit(self.surface, (self.x, self.y))

    def return_x(self):
        return self.x