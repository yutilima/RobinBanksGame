from PPlay.sprite import *
from PPlay.collision import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sound import *
import math
import random

from Player import *
from Shot import Shot
from Cop import Cop
from Moneybag import moneybag
from controles import *
from game_over import gameover
from caixa import *

def jogo(tela):

    janela = tela
    surface = pygame.Surface((janela.width, janela.height), pygame.SRCALPHA)
    fundo = pygame.image.load("Assets/menu/fundoescuro.png")
    mapa = GameImage('Assets/Mapa.png')
    intro = True
    transparencia = 255
    dtm = 0.01
    shadows = Sprite('Assets/sombras.png')
    teclado = janela.get_keyboard()
    mouse = janela.get_mouse()
    bounding = Sprite("Assets/Player_Bounding.png")
    dano_fx = Sprite("Assets/efeito_dano.png")
    cont_dano = 2


    while intro:
        if transparencia < 255:
            mapa.draw()
            shadows.draw()
        surface.set_alpha(transparencia)
        janela.screen.blit(surface, (0, 0))
        surface.blit(fundo, (0, 0))
        #pygame.draw.rect(surface, (255, 0, 0, 120), [100, 200, 300, 400])
        janela.update()
        dtm = janela.delta_time()
        if transparencia > 1:
            transparencia -= 200*dtm
        else: intro = False









    def grau_mouse(mouse_coord, ref_coord):
        return math.degrees(math.atan2(-mouse_coord[1] + ref_coord[1], mouse_coord[0] - ref_coord[0]))

    def grau_cop(ref_coord, cop_coord):
        return math.degrees(math.atan2(cop_coord[1] - ref_coord[1], ref_coord[0] - cop_coord[0]))

    def colisor(sprite, ref_coord):
        c = Sprite(sprite)
        c.x = ref_coord[0]
        c.y = ref_coord[1]
        return c

    def criar_horda_right(dist, dif):
        for i in range(2 + dif):
            policiais_right.append(Cop(pygame.image.load("Assets\cop2.png"), (1500 + dist*i, (janela.height/2)-dist), janela.screen))
            policiais_right.append(Cop(pygame.image.load("Assets\cop2.png"), (1500 + dist*i, janela.height/2), janela.screen))
            policiais_right.append(Cop(pygame.image.load("Assets\cop2.png"), (1500 + dist*i, (janela.height/2)+dist), janela.screen))
        for i in range(len(policiais_right)):
            policiais_right[i].shot_cooldown = random.randint(0, 200)/100

    def criar_horda_left(dist, dif):
        for i in range(2 + dif):
            policiais_left.append(Cop(pygame.image.load("Assets\cop2.png"), (-200 + dist*i, (janela.height/2)-dist), janela.screen))
            policiais_left.append(Cop(pygame.image.load("Assets\cop2.png"), (-200 + dist*i, janela.height/2), janela.screen))
            policiais_left.append(Cop(pygame.image.load("Assets\cop2.png"), (-200 + dist*i, (janela.height/2)+dist), janela.screen))
        for i in range(len(policiais_left)):
            policiais_left[i].shot_cooldown = random.randint(0, 200)/100

    def mov_horda_right(speed, dtime, fase):
        menor_x = 1500
        if fase == 1:
            for i in range(len(policiais_right)):
                if policiais_right[i].x < menor_x and policiais_right[i].vivo == True:
                    menor_x = policiais_right[i].x
            if menor_x >= 1100:
                for i in range(len(policiais_right)):
                    if policiais_right[i].vivo == True:
                        policiais_right[i].move(-speed*dtime, 0)

    def mov_horda_left(speed, dtime, fase):
        maior_x = -200
        if fase == 1:
            for i in range(len(policiais_left)):
                if policiais_left[i].x > maior_x and policiais_left[i].vivo == True:
                    maior_x = policiais_left[i].x
            if maior_x <= 200:
                for i in range(len(policiais_left)):
                    if policiais_left[i].vivo == True:
                        policiais_left[i].move(speed*dtime, 0)




    player = Player(pygame.image.load("Assets\Player.png"), (janela.width/2, janela.height - 300), janela.screen)

    player_speed_base = 200
    player_speed = player_speed_base

    sentinelas_speed = 50
    policiais_speed = 100
    policiais_left = []
    policiais_left_fase = 1
    policiais_right = []
    policiais_right_fase = 1
    tiros = []
    tiros_cop = []
    colisores =[]
    moneybags = []
    policiais_vivos = 0
    pob_shot_cop = 10
    cooldown_cop = 1
    alarme = False
    money_click = False
    drop_distace = 50
    money = 0
    pontos = 0
    cooldown_caixas = 5
    dificuldade = 0
    arma = 0
    timer = 30





    colisores =[]
    colisores.append(colisor('Assets/parede_vertical.png', (0,0)))
    colisores.append(colisor('Assets/parede_vertical.png', (1280,0)))
    colisores.append(colisor('Assets/parede_horizontal.png', (71,0)))
    colisores.append(colisor('Assets/parede_horizontal.png', (71,980)))
    colisores.append(colisor('Assets/caixa_eletronico.png', (71,292)))
    colisores.append(colisor('Assets/caixa_eletronico.png', (71,175)))
    colisores.append(colisor('Assets/caixa_eletronico2.png', (175, 70)))
    colisores.append(colisor('Assets/caixa_eletronico2.png', (292, 70)))
    colisores.append(colisor('Assets/caixa_eletronico2.png', (410, 70)))
    colisores.append(colisor('Assets/sala.png',(585, 70)))
    colisores.append(colisor('Assets/bush1.png',(84, 635)))
    colisores.append(colisor('Assets/bush2.png',(515, 688)))
    colisores.append(colisor('Assets/bush1.png',(776, 635)))
    colisores.append(colisor('Assets/bush2.png',(776, 688)))
    colisores.append(colisor('Assets/bush2.png',(55, 61)))
    colisores.append(colisor('Assets/bush2.png',(112, 61)))
    colisores.append(colisor('Assets/bush2.png',(55, 114)))
    colisores.append(colisor('Assets/bush3.png',(517, 70)))
    colisores.append(colisor('Assets/poltronas.png',(200, 812)))
    colisores.append(colisor('Assets/poltronas.png',(395, 812)))
    colisores.append(colisor('Assets/poltronas.png',(863, 812)))
    colisores.append(colisor('Assets/poltronas.png',(1055, 812)))
    colisores.append(colisor('Assets/mesa.png',(195, 764)))
    colisores.append(colisor('Assets/mesa.png',(195, 716)))
    colisores.append(colisor('Assets/mesa.png',(862, 764)))
    colisores.append(colisor('Assets/mesa.png',(862, 716)))

    #cria caixas:
    caixas = [None]*5
    caixas[0] = (caixa(pygame.image.load('Assets/coleta3fechado.png'), (133, 338), janela.screen))
    caixas[1] = (caixa(pygame.image.load('Assets/coleta3fechado.png'), (132, 221), janela.screen))
    caixas[2] = (caixa(pygame.image.load('Assets/coleta3fechado.png'), (192, 135), janela.screen))
    caixas[3] = (caixa(pygame.image.load('Assets/coleta3fechado.png'), (309, 134), janela.screen))
    caixas[4] = (caixa(pygame.image.load('Assets/coleta3fechado.png'), (428, 134), janela.screen))

    sentinelas = []
    sentinelas.append(Cop(pygame.image.load("Assets/lanterninha.png"), (200, 500), janela.screen))
    sentinelas[0].grau = 90
    sentinelas.append(Cop(pygame.image.load("Assets/lanterninha.png"), (679, 524), janela.screen))
    sentinelas[1].grau = 360
    sentinela1_check = False
    crono_sentinela1 = 0
    grau_rodado_sentinela1 = 0

    ponto_coleta = colisor('Assets/coleta2.png', (625, 917))
    drop_sfx = Sound('Assets/drop.ogg')
    collect_sfx = Sound('Assets/collect.ogg')
    money_sfx = Sound('Assets/money.ogg')

    #sons:
    shot_sfx = Sound("Assets/som_tiro.ogg")
    shot_sfx.set_volume(25)
    shot_police_sfx = Sound("Assets/som_tiro.ogg")
    shot_police_sfx.set_volume(15)
    walk_sfx = Sound("Assets/walking_sfx.ogg")
    cont_walk = 0
    #GAMELOOP
    run = True
    while(run):
        dtime = janela.delta_time()

        if(teclado.key_pressed("1")):
            arma = 0
        elif(teclado.key_pressed("2") and dificuldade >= 2):
            arma = 1

        

        timer -= dtime
        if((player_speed - money) > 100):
            player_speed = 200 - money

        #condicoes de parada:
        if teclado.key_pressed("escape"):
            run = False
        if player.vida <= 0 or timer <= 0:
            gameover(janela, pontos)
            run = False

        girar(player, mouse)
        
        bounding.x = player.x - player.height/2
        bounding.y = player.y - player.height/2
        
        #Controles Do Jogador
        atirar(player, mouse, tiros, dtime, janela, shot_sfx, arma)
        mover(player, teclado, player_speed, player_speed_base, dtime)
        cont_walk += dtime
        if(cont_walk >= 0.5 and (teclado.key_pressed("w") or teclado.key_pressed("a") or teclado.key_pressed("s") or teclado.key_pressed("d"))):
            walk_sfx.play()
            cont_walk = 0

        mapa.draw()

        #POLICIAIS:
        #inicio do alarme
        #sentinelas:
        for i in range(len(sentinelas)-1, -1, -1):
            sentinelas[i].set_rotation(sentinelas[i].grau)
            if alarme == False:
                #ROTA DO SENTINELA 1
                if sentinelas[0].x <= 216 and sentinelas[0].y >= 233:
                    if sentinelas[0].grau >= 90:
                        sentinelas[0].grau -= 60*dtime
                    else:
                        sentinelas[0].y -= sentinelas_speed*dtime
                if sentinelas[0].y <= 233 and sentinelas[0].x <= 490:
                    if sentinelas[0].grau >= 0 and sentinelas[0].grau <= 180:
                        sentinelas[0].grau -= 60*dtime
                    else:
                        sentinelas[0].x += sentinelas_speed*dtime
                        sentinelas[0].grau = 360
                if sentinelas[0].x >= 490 and sentinelas[0].y <= 570:
                    if sentinelas[0].grau >= 270:
                        sentinelas[0].grau -= 100*dtime
                    else:
                        sentinelas[0].y += sentinelas_speed*dtime
                if sentinelas[0].y >= 570 and sentinelas[0].x >=216:
                    if sentinelas[0].grau >= 180:
                        sentinelas[0].grau -= 60*dtime
                    else:
                        sentinelas[0].x -= sentinelas_speed*dtime

                #ROTA DO SENTINELA 2:
                crono_sentinela1 += dtime
                if(crono_sentinela1 > 3):
                    if grau_rodado_sentinela1 < 90:
                        sentinelas[1].grau += 60*dtime
                        grau_rodado_sentinela1 += 60*dtime
                    else:
                        grau_rodado_sentinela1 = 0
                        crono_sentinela1 = 0


                if(player.collideR(sentinelas[i]) or mouse.is_button_pressed(1)):
                    alarme = True
            else:
                #acao sentinelas:
                sentinelas[i].set_rotation(grau_cop((player.x, player.y), (sentinelas[i].x, sentinelas[i].y)))
                sentinelas[i].shot_cooldown += dtime
            for j in range(len(tiros)-1, -1, -1):
                if(sentinelas[i].collideR(tiros[j])):
                    del sentinelas[i]
                    del tiros[j]
                    break

            

        mov_horda_right(policiais_speed, dtime, policiais_right_fase)
        mov_horda_left(policiais_speed, dtime, policiais_left_fase)
        if alarme == True and policiais_vivos == 0:
            policiais_right.clear()
            policiais_left.clear()
            criar_horda_left(50, dificuldade)
            criar_horda_right(50, dificuldade)
            timer = 30
        policiais_vivos = 0


        #CAIXAS:
        for i in range(len(caixas)):
            caixas[i].draw()
            if(player.collideR(caixas[i])):
                if(caixas[i].open == False and teclado.key_pressed("e")):
                    pygame.draw.rect(tela.screen, (20, 0, 250), (caixas[i].nx, caixas[i].ny+50, 50, 10))
                    pygame.draw.rect(tela.screen, (0, 255, 0), (caixas[i].nx, caixas[i].ny+50, caixas[i].op_time*(50/3), 10))
                    caixas[i].op_time += dtime
                    if caixas[i].op_time >= 3:
                        caixas[i].open = True
                        caixas[i].superf = pygame.image.load('Assets/coleta3.png')
                        if alarme==False: alarme = True
                else: caixas[i].op_time = 0
                if(caixas[i].open == True):
                    if(caixas[i].money_cooldown >= cooldown_caixas and teclado.key_pressed("e")):
                        moneybags.append(moneybag(pygame.image.load("Assets\moneybag.png"), (caixas[i].nx, caixas[i].ny + 60), janela.screen))
                        caixas[i].money_cooldown = 0
                        money_sfx.play()
            if caixas[i].open == True:
                caixas[i].money_cooldown += dtime
                    
                    

        #MONEYBAGS:
        for i in range(len(moneybags)):
            if(moneybags[i].got == False):
                moneybags[i].draw()
            #pegar:
            if(moneybags[i].got == False and player.collideR(moneybags[i]) and teclado.key_pressed("e")):
                moneybags[i].got = True
                collect_sfx.play()
                money += 10
            #Soltar
            if(moneybags[i].got == True and money_click == False and teclado.key_pressed("q")):
                money_click = True
                moneybags[i].nx = (player.x + (drop_distace * math.sin(math.atan2((-mouse.get_position()[1] + player.y), (mouse.get_position()[0] - player.x))+math.pi/2))) - moneybags[i].width/2
                moneybags[i].ny = (player.y + (drop_distace * math.cos(math.atan2((-mouse.get_position()[1] + player.y), (mouse.get_position()[0] - player.x))+math.pi/2))) - moneybags[i].height/2
                moneybags[i].got = False
                drop_sfx.play()
                money -= 10
            if(money_click == True and not teclado.key_pressed("q")):
                money_click = False

        #Drop:


        #Tiros:
        for i in range(len(tiros)-1, -1, -1):
            tiros[i].trajetoria(dtime)
            tiros[i].draw()
            for j in range(len(colisores)):
                if Collision.collided(tiros[i], colisores[j]):
                    del tiros[i]
                    break

        for i in range(len(tiros_cop)-1, -1, -1):
            tiros_cop[i].trajetoria(dtime)
            tiros_cop[i].draw()
            if player.collideR(tiros_cop[i]):
                player.vida -= 5
                cont_dano = 0
                del tiros_cop[i]
                
                continue
            for j in range(len(colisores)):
                if Collision.collided(tiros_cop[i], colisores[j]):
                    del tiros_cop[i]
                    break
        if(cont_dano < 100):
            cont_dano += dtime
        if(cont_dano < 0.1):
            dano_fx.draw()


        #sentinelas:
        for i in range(len(sentinelas)):
            sentinelas[i].draw()

        #horda da right:
        for i in range(len(policiais_right)):
            if policiais_right[i].vivo == False: policiais_right[i].draw()
        for i in range(len(policiais_right)):
            if policiais_right[i].vivo == True:
                policiais_vivos += 1
                policiais_right[i].set_rotation(grau_cop((player.x, player.y), (policiais_right[i].x, policiais_right[i].y)))
                policiais_right[i].shot_cooldown += dtime
                #TIRO POLICIAL:
                if(policiais_right[i].shot_cooldown > cooldown_cop):
                    if (random.randint(0, 100) < pob_shot_cop):
                        tiros_cop.append(Shot(pygame.image.load("Assets\shot.png"), (policiais_right[i].x, policiais_right[i].y), (player.x, player.y), janela.screen))
                        shot_police_sfx.play()
                    policiais_right[i].shot_cooldown = 0
                policiais_right[i].draw()
            #COLISAO COM OS TIROS DO PLAYER
            for j in range(len(tiros)-1, -1, -1):
                if(policiais_right[i].collideR(tiros[j]) and policiais_right[i].vivo == True):
                    policiais_right[i] = Cop(pygame.image.load("Assets/DeadCop.png"), (policiais_right[i].x, policiais_right[i].y), janela.screen)
                    policiais_right[i].vivo = False
                    del tiros[j]

        #horda left:
        for i in range(len(policiais_left)):
            if policiais_left[i].vivo == False: policiais_left[i].draw()
        for i in range(len(policiais_left)):
            if policiais_left[i].vivo == True:
                policiais_left[i].set_rotation(grau_cop((player.x, player.y), (policiais_left[i].x, policiais_left[i].y)))
                policiais_left[i].draw()
                policiais_vivos += 1
                policiais_left[i].shot_cooldown += dtime
                #TIRO POLICIAL:
                if(policiais_left[i].shot_cooldown > cooldown_cop):
                    if (random.randint(0, 100) < pob_shot_cop):
                        tiros_cop.append(Shot(pygame.image.load("Assets\shot.png"), (policiais_left[i].x, policiais_left[i].y), (player.x, player.y), janela.screen))
                        shot_police_sfx.play()
                    policiais_left[i].shot_cooldown = 0
            #COLISAO COM OS TIROS DO PLAYER
            for j in range(len(tiros)-1, -1, -1):
                if(policiais_left[i].collideR(tiros[j]) and policiais_left[i].vivo == True):
                    policiais_left[i] = Cop(pygame.image.load("Assets/DeadCop.png"), (policiais_left[i].x, policiais_left[i].y), janela.screen)
                    policiais_left[i].vivo = False
                    del tiros[j]


        for c in range(len(colisores)):

            c_x_start = colisores[c].x
            c_x_end = c_x_start + colisores[c].width
            c_y_start = colisores[c].y
            c_y_end = c_y_start + colisores[c].height

            b_x_start = bounding.x
            b_x_end = b_x_start + bounding.width
            b_y_start = bounding.y
            b_y_end =b_y_start + bounding.height

            bounce_back =  player_speed*dtime #10*player.width*dtime

            if((c_x_start <= b_x_start <= c_x_end) and ((c_y_start <= b_y_start <= c_y_end) or (c_y_start <= b_y_end <= c_y_end))):
                #print("Colisão à Esquerda")
                player.move(bounce_back, 0)
            if((c_x_start <= b_x_end <= c_x_end) and ((c_y_start <= b_y_start <= c_y_end) or (c_y_start <= b_y_end <= c_y_end))):
                #print("Colisão à Direita")
                player.move(-bounce_back,0)
            if((c_y_start <= b_y_start <= c_y_end)) and  ((c_x_start <= b_x_start <= c_x_end) or (c_x_start <= b_x_end <= c_x_end)):
                #print("Colisão Acima")
                player.move(0,bounce_back)
            if((c_y_start <= b_y_end <= c_y_end)) and ((c_x_start <= b_x_start <= c_x_end) or (c_x_start <= b_x_end <= c_x_end)):
                #print("Colisão Abaixo")
                player.move(0, -bounce_back)

        if(Collision.collided(ponto_coleta, player) and money > 0):
            pontos += money
            vida_extra = int(money*0.25)
            money = 0
            drop_sfx.play()
            
            for m in range(len(moneybags)-1,-1,-1): 
                if(moneybags[m].got == True): del(moneybags[m])
            if(dificuldade < 3): dificuldade+=1
            if(pob_shot_cop < 30): pob_shot_cop += 5
            if(player.vida + vida_extra <= 100): player.vida += vida_extra


    
        ponto_coleta.draw()
        player.draw()
        shadows.draw()
        #bounding.draw()
        #for i in range(len(colisores)): colisores[i].draw()

        janela.draw_text(f'Tempo Restante: {int(timer)}s', 60, 60, 40, (255,255,255),'Arial',True, False)

        janela.draw_text(f'$ {money}.00',1200, 60, 25, (33, 150, 70), 'Arial', True, False)
        pygame.draw.rect(tela.screen, (255, 0, 0), (1200, 100, 100, 10))
        pygame.draw.rect(tela.screen, (0, 255, 0), (1200, 100, player.vida, 10))
        
        if arma == 0:
            janela.draw_text("Pistola" ,1200, 120, 25, (0, 0, 0), 'Arial', True, False)
        else:
            janela.draw_text("Escopeta" ,1200, 120, 25, (0,0,0), 'Arial', True, False)
        
        janela.update()