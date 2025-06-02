import pygame
    
    
    
    
class caixa:
    def __init__(self, superf, coord, tela):
        self.superf = superf
        self.tela = tela
        self.nx = coord[0]
        self.ny = coord[1]
        self.mask = pygame.mask.from_surface(self.superf)
        self.rect = superf.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.open = False
        self.op_time = 0
        self.money_cooldown = 0

    def abrir(self, dtime):
        pass

    def draw(self):
        self.tela.blit(self.superf, (self.nx, self.ny))
