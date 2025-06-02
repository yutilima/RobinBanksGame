from Shot import *
from PPlay.sound import *

def duas_teclas_pressionadas(teclado):
    
    if(teclado.key_pressed("w") and teclado.key_pressed("a")): return True

    elif(teclado.key_pressed("w") and teclado.key_pressed("d")): return True
    
    elif(teclado.key_pressed("s") and teclado.key_pressed("a")):  return True

    elif(teclado.key_pressed("s") and teclado.key_pressed("d")):  return True

    else: return False

def grau_mouse(mouse_coord, ref_coord):
    return math.degrees(math.atan2(-mouse_coord[1] + ref_coord[1], mouse_coord[0] - ref_coord[0]))

def atirar(player, mouse, tiros, dtime, janela, som_tiro, gun):
    if(mouse.is_button_pressed(1) and player.shot_cooldown <= 0):
        #cria tiro como um attach do mapa(se move junto com o mapa dentro da classe mapa)
        if gun == 0:
            tiros.append(Shot(pygame.image.load("Assets\shot.png"), (player.x, player.y), mouse.get_position(), janela.screen))
            player.shot_cooldown = 1
            som_tiro.play()
        elif gun == 1:
            tiros.append(Shot(pygame.image.load("Assets\shot.png"), (player.x, player.y), (mouse.get_position()[0] + 20, mouse.get_position()[1] + 20), janela.screen))
            tiros.append(Shot(pygame.image.load("Assets\shot.png"), (player.x, player.y), (mouse.get_position()[0] + 40, mouse.get_position()[1] + 40), janela.screen))
            tiros.append(Shot(pygame.image.load("Assets\shot.png"), (player.x, player.y), (mouse.get_position()[0] - 20, mouse.get_position()[1] - 20), janela.screen))
            tiros.append(Shot(pygame.image.load("Assets\shot.png"), (player.x, player.y), (mouse.get_position()[0] - 40, mouse.get_position()[1] - 40), janela.screen))
            player.shot_cooldown = 1
            som_tiro.play()
    player.shot_cooldown -= dtime

def mover(player, teclado, player_speed, player_speed_base, dtime):

    if(duas_teclas_pressionadas(teclado) and player_speed > player_speed_base/2): player_speed /= 2

    if(teclado.key_pressed("w")):
        player.move(0,-player_speed*dtime)

    if(teclado.key_pressed("a")):
        player.move(-player_speed*dtime, 0)

    if(teclado.key_pressed("s")):
        player.move(0, player_speed*dtime)

    if(teclado.key_pressed("d")):
        player.move(player_speed*dtime, 0)
    

    player_speed = player_speed_base

def girar(player, mouse): 
    player.set_rotation(grau_mouse(mouse.get_position(), (player.x, player.y)))