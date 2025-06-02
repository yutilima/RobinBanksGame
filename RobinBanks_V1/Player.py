from PPlay.sprite import *
from PPlay.collision import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *


class Player:
    def __init__(self, superf,coord, tela):
        self.x = coord[0]
        self.y = coord[1]
        #Centraliza a imagem:
        self.nx = self.x - superf.get_width()/2
        self.ny = self.y - superf.get_height()/2
        self.superf = superf
        #Superficie de backup para nao distorcer a superficie original:
        self.backup_superf = superf
        self.tela = tela
        self.vida = 100
        self.grau = 0
        self.mask = pygame.mask.from_surface(self.superf)
        self.shot_cooldown = 0.7
        self.money = 0
        self.width = superf.get_width()
        self.height = superf.get_height()
        self.vida = 100

    def move(self, x, y):
        self.x += x
        self.y += y

    
    def set_rotation(self, grau):
        self.grau = grau
        self.superf = self.backup_superf
        self.superf = pygame.transform.rotate(self.superf, grau-75)
        self.mask = pygame.mask.from_surface(self.superf)
    
    def draw(self):
        #Centraliza tomando como base x e y da imagem:
        self.nx = self.x - self.superf.get_width()/2
        self.ny = self.y - self.superf.get_height()/2
        #Da o blit usando a nova posicao como referencia:
        self.tela.blit(self.superf, (self.nx, self.ny))

    def collideR(self, objeto):
        offset_x = (int(objeto.nx - self.nx))
        offset_y = (int(objeto.ny - self.ny))
        if(self.mask.overlap(objeto.mask, (offset_x, offset_y)) != None):
            return True
        else: return False
