from PPlay.sprite import *
from PPlay.collision import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *

class moneybag:
    def __init__(self, superf, coord, tela):
        self.superf = superf
        self.tela = tela
        self.nx = coord[0]
        self.ny = coord[1]
        self.mask = pygame.mask.from_surface(self.superf)
        self.got = False
        self.rect = superf.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

    def draw(self):
        if(not self.got):
            self.tela.blit(self.superf, (self.nx, self.ny))
