import pygame
import map
import button
import easygui

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
        self.map = None
        self.state = MENU

        new_btn_img = pygame.image.load("../assets/button.png")
        new_btn_clk = pygame.image.load("../assets/buttonclicked.png")
        new_btn_hvr = pygame.image.load("../assets/buttonhover.png")
        self.new_game_btn = button.Button(new_btn_img, new_btn_hvr, new_btn_clk, (250, 600),
                                          self.on_btn_click, "new_game")

        load_btn_img = pygame.image.load("../assets/button.png")
        load_btn_clk = pygame.image.load("../assets/buttonclicked.png")
        load_btn_hvr = pygame.image.load("../assets/buttonhover.png")
        self.load_game_btn = button.Button(load_btn_img, load_btn_hvr, load_btn_clk, (750, 600),
                                           self.on_btn_click, "load_game")

    def event_update(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.new_game_btn.on_release(event)
                    self.load_game_btn.on_release(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.new_game_btn.on_click(event)
                    self.load_game_btn.on_click(event)
            if event.type == pygame.MOUSEMOTION:
                self.new_game_btn.on_hover(event)
                self.load_game_btn.on_hover(event)

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
            self.load_game_btn.disabled = True
            self.screen.fill((0, 0, 0))
            map_json = self.map.get_whole_map()
            map_sz = self.map.get_map_size()
            for y in range(map_sz[1]):
                for x in range(map_sz[0]):
                    if x % 2:
                        real_x = x * 0.5 * 128
                        real_y = y * 64 - 447
                        if map_json["map"][x][y]["type"] != "air":
                            image = pygame.image.load("../assets/" + map_json["map"][x][y]["type"] + ".png")
                            self.screen.blit(image, (real_x, real_y))
                for x in range(map_sz[0]):
                    if not x % 2:
                        real_x = x * 0.5 * 128
                        real_y = (y + 0.5) * 64 - 447
                        if map_json["map"][x][y]["type"] != "air":
                            image = pygame.image.load("../assets/" + map_json["map"][x][y]["type"] + ".png")
                            self.screen.blit(image, (real_x, real_y))

        else:
            self.new_game_btn.disabled = False
            self.load_game_btn.disabled = False
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.new_game_btn.image, self.new_game_btn.rect)
            self.screen.blit(self.load_game_btn.image, self.load_game_btn.rect)

    def update(self):
        pygame.display.flip()

    def fps(self, fps):
        self.clock.tick(fps)

    def on_btn_click(self, btn):
        if btn.name == "new_game":
            file = easygui.filesavebox(None, "Create new Game", "*.sav", ["*.sav", "SAV files"])
            if file is not None:
                self.map = map.Map(file)
                self.map.gen_new_map(20, 20)
                self.state = GAME
        if btn.name == "load_game":
            file = easygui.fileopenbox(None, "Load Game", "*.sav", ["*.sav", "SAV files"])
            if file is not None:
                self.map = map.Map(file)
                self.state = GAME
