from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *

def gameover(screen, score):
    janela = screen
    run = True
    texto = Sprite("Assets\game_over.png")
    texto.x = 198
    texto.y = 251
    teclado = janela.get_keyboard()
    while run:
        if(teclado.key_pressed("escape")):
            run = False
        janela.set_background_color(0)
        texto.draw()
        janela.draw_text((f"Valor Arrecadado: $ {score}.000,00"), 198, 251 + texto.height*2, 80, (255, 0, 0), "Gang Avenue")
        janela.update()