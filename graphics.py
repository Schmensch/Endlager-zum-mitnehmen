import pygame


size = width, height = 1000, 800


class Graphics:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size)

        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill((255, 255, 0))

    def update(self):
        pygame.display.flip()

    def fps(self, fps):
        self.clock.tick(fps)
