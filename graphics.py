import pygame
import map


QUIT = 1

size = width, height = 1000, 800


class Graphics:
    def __init__(self, map_safe):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Endlager zum mitnehmen")
        self.clock = pygame.time.Clock()
        self.map = map.Map(map_safe)

    def event_update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT

    def set_tile(self, map_x, map_y, tile):
        real_x = map_x * 0.5 * 128
        real_y = map_y * 0.5 * 64 - 447
        print(real_x, real_y)
        image = pygame.image.load("../assets/" + tile["type"] + ".png")
        self.screen.blit(image, (real_x, real_y))
        self.map.set_tile(map_x, map_y, tile)

    def draw(self):
        pass

    def update(self):
        pygame.display.flip()

    def fps(self, fps):
        self.clock.tick(fps)
