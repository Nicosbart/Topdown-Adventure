import pygame as pg
from settings import *


class Map():
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as file:
            for line in file:
                self.data.append(line)

        self.tilewidht = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidht * TILESIZE
        self.height = self.tileheight * TILESIZE


class Camera():
    def __init__(self, width=WIDTH, height=HEIGHT):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.left = 0
        self.right = width
        self.bottom = height
        self.top = 0

    def apply(self, other):
        return other.rect.move(self.camera.topleft)

    def update(self, player):
        x, y = self.camera.topleft

        print(f'player x, y: {player.pos.x}, {player.pos.y}')
        print(f'player rect l, r: {player.rect.left}, {player.rect.right}')
        print(f'left/right: {self.left}, {self.right}')
        print(f'camera left, right: {self.camera.left}, {self.camera.right}')
        print()

        if player.rect.right >= self.right and player.vel.x > 0:
            x -= self.width
            self.left += self.width
            self.right += self.width
            player.pos.x += 3*player.image.get_width()/2
        elif player.rect.left <= self.left and player.vel.x < 0:
            x += self.width
            self.left -= self.width
            self.right -= self.width
            player.pos.x -= 3*player.image.get_width()/2
        elif player.rect.bottom >= self.bottom and player.vel.y > 0:
            y -= self.height
            self.bottom += self.height
            self.top += self.height
            player.pos.y += 3*player.image.get_width()/2
        elif player.rect.top <= self.top and player.vel.y < 0:
            y += self.height
            self.bottom -= self.height
            self.top -= self.height
            player.pos.y -= 3*player.image.get_width()/2

        self.camera = pg.Rect(x, y, self.width, self.height)
