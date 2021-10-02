from settings import HEIGHT, WIDTH
import pygame as pg
from settings import *
from sprites import *
from map import *
from os import path


class Game():
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.wall_group = pg.sprite.Group()
        
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'w':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, row, col)
        self.camera = Camera()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False
            if event.type == pg.QUIT:
                self.playing = False

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, 'map.txt'))
        

    def update(self):
        self.all_sprites.update()
        self.wall_group.update()
        self.camera.update(self.player)

    def draw(self):
        self.screen.fill(DARKGREY)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()

        pg.quit()


if __name__ == '__main__':
    game = Game()
    game.new()
    game.run()
