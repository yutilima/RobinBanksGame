from PPlay.sprite import *
from PPlay.collision import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
import math

class Shot():
    def __init__(self, superf, coord, dest_coord, tela):
        self.superf = superf
        self.image = self.superf
        self.x = coord[0]
        self.y = coord[1]
        #centraliza o tiro:
        self.nx = self.x - superf.get_width()/2
        self.ny = self.y - superf.get_height()/2
        self.speed = 1000
        #Calculamos a direcao que o tiro toma multiplicada pela velocidade
        self.vx = self.speed * math.sin(math.atan2((-dest_coord[1] + coord[1]), (dest_coord[0] - coord[0]))+math.pi/2)
        self.vy  = self.speed * math.cos(math.atan2((-dest_coord[1] + coord[1]), (dest_coord[0] - coord[0]))+math.pi/2)
        self.tela = tela
        self.mask = pygame.mask.from_surface(superf)
        self.hit = False
        self.rect = superf.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

    def trajetoria(self, dtime):
        self.x += self.vx * dtime
        self.y += self.vy * dtime

    def draw(self):
        #calcula o nx e ny(posicao relativa para que o x e o y estejam no CENTRO do objeto)
        self.nx = self.x - self.superf.get_width()/2
        self.ny = self.y - self.superf.get_height()/2
        self.tela.blit(self.superf, (self.nx, self.ny))