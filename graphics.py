import pygame


QUIT = 1

size = width, height = 1000, 800


class Graphics:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Endlager zum mitnehmen")

        self.clock = pygame.time.Clock()

    def event_update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT

    def draw(self):
        self.screen.fill((255, 255, 0))

    def update(self):
        pygame.display.flip()

    def fps(self, fps):
        self.clock.tick(fps)
