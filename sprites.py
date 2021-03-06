import pygame as pg
from settings import*
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE

    def update(self):
        self.get_keys()
        self.move(self.vel)

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.vel.x += PLAYER_SPEED* self.game.dt
        if keys[pg.K_LEFT]:
            self.vel.x -= PLAYER_SPEED* self.game.dt
        if keys[pg.K_UP]:
            self.vel.y -= PLAYER_SPEED* self.game.dt
        if keys[pg.K_DOWN]:
            self.vel.y += PLAYER_SPEED* self.game.dt
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

    def move(self, vel=(0, 0)):
        if not self.collide_with_walls(vel):
            self.pos += vel
            self.rect.x = self.pos.x
            self.collide_with_walls('x')
            self.rect.y = self.pos.y
            self.collide_with_walls('y')
        

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.wall_group, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left  - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right

                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.wall_group, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top  - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom

                self.vel.y = 0
                self.rect.y = self.pos.y
            


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.wall_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.topleft = self.pos * TILESIZE

