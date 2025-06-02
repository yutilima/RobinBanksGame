from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from jogo import *
from PPlay.sound import*
import time

contador = 0


janela = Window(1350, 1050)
fundo = GameImage("Assets\menu/fundoescuro.png")
mouse = janela.get_mouse()
teclado = janela.get_keyboard()
robin = Sprite("Assets/menu/ROBIN.png")
robin.y = 101
robin.x = -robin.width
banks = Sprite("Assets/menu/BANKS.png")
banks.y = 192
banks.x = janela.width
jogar_b = Sprite("Assets/menu/JOGAR.png")
jogar_b.x = janela.width/2 - jogar_b.width/2
jogar_b.y = janela.height + 300

music = Sound('Assets/musica.ogg')
music.set_repeat(True)
music.set_volume(15)
music.play()
timer = 3
dtime = 0.01
run = True
while(run):
    if(teclado.key_pressed("escape")): run = False
    fundo.draw()
    if timer >= 0: timer -= dtime
    if(timer <= 0):
        if(robin.x < 154):
            robin.x += (1000*dtime)
        if(banks.x > 675):
            banks.x -= (1000*dtime)
        if(jogar_b.y > 475):
            jogar_b.y -= (100*dtime)
        
        if(mouse.is_over_object(jogar_b)):
            jogar_b = Sprite("Assets/menu/JOGAR2.png")
            jogar_b.x = janela.width/2 - jogar_b.width/2
            jogar_b.y = 475
            if(mouse.is_button_pressed(1)):
                jogo(janela)
                pass
        else:
            jogar_b = Sprite("Assets/menu/JOGAR.png")
            jogar_b.x = janela.width/2 - jogar_b.width/2
            jogar_b.y = 475

    
    jogar_b.draw()
    banks.draw()
    robin.draw()
    dtime = janela.delta_time()
    janela.update()
