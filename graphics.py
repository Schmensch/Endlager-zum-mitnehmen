import pygame
import map
import button

QUIT = 1
MENU = 0
GAME = 2


size = width, height = 1000, 800


class Graphics:
    def __init__(self, map_safe):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Endlager zum mitnehmen")
        self.clock = pygame.time.Clock()
        self.map = map.Map(map_safe)
        self.state = MENU

        btn_img = pygame.image.load("../assets/button.png")
        self.new_game_btn = button.Button(btn_img, (250, 600), self.on_btn_click, "new_game")


    def event_update(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.new_game_btn.on_click(event)

    def set_tile(self, map_x, map_y, tile):
        real_x = map_x * 0.5 * 128
        real_y = map_y * 0.5 * 64 - 447
        print(real_x, real_y)
        self.map.set_tile(map_x, map_y, tile)

    def dialog(self, title, subtitle, text, options):
        pass

    def draw(self):

        if self.state == GAME:
            self.new_game_btn.disabled = True
            self.screen.fill((0, 0, 0))
            map_json = self.map.get_whole_map()
            for x in range(len(map_json["map"])):
                for y in range(len(map_json["map"][x])):
                    real_x = x * 0.5 * 128
                    real_y = y * 0.5 * 64 - 447
                    if map_json["map"][x][y]["type"] != "air":
                        image = pygame.image.load("../assets/" + map_json["map"][x][y]["type"] + ".png")
                        self.screen.blit(image, (real_x, real_y))

        else:
            self.new_game_btn.disabled = False
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.new_game_btn.image, self.new_game_btn.rect)


    def update(self):
        pygame.display.flip()

    def fps(self, fps):
        self.clock.tick(fps)

    def on_btn_click(self, test):
        print(test.name)

