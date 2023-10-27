import pygame, pgzero, pgzrun
from genetica import Pessoa, PessoaRANDOM

WIDTH = 1700
HEIGHT = 800

#   Generos: masc, fem
#   Tipos de cabelo MASC: curto, medio, longo, americano
#   Tipos de cabelo FEM: rabo, sidecut, solto, black
#   Cores de cabelo: ruivo, castanho, loiro
#   Cores de olhos: azul, castanho, verde

pessoas_masc = {}
pessoas_fem = {}
filho = None
frame_m = None
frame_f = None

fundo = Actor('fundo.png')
for i in range(0,4):
    pessoas_masc[i] = PessoaRANDOM('masc')
    pessoas_fem[i] = PessoaRANDOM('fem')

print(len(pessoas_fem))

#colisoes
colisao_m1 = Rect(93,216, 256, 256)
colisao_m2 = Rect(349,216, 256, 256)
colisao_m3 = Rect(605,216, 256, 256)
colisao_m4 = Rect(861,216, 256, 256)
colisao_f1 = Rect(93,501, 256, 256)
colisao_f2 = Rect(349,501, 256, 256)
colisao_f3 = Rect(605,501, 256, 256)
colisao_f4 = Rect(861,501, 256, 256)
frame_selecionadoM = Actor('frame_selecao')
frame_selecionadoM.pos = (1000,1000)
frame_selecionadoF = Actor('frame_selecao')
frame_selecionadoF.pos = (1000,1000)
gerar = Rect(1315,526, 261, 90)
reset = Rect(1315,638, 261, 90)

def draw():
    global filho, frame_selecionadoM
    screen.fill((255,255,255))
    fundo.draw()
    for i in range(0,4):
        desenharpessoa(pessoas_masc[i], 221+(256*i), 339)
        desenharpessoa(pessoas_fem[i], 221+(256*i), 624)
    frame_selecionadoM.draw()
    frame_selecionadoF.draw()
    if filho != None:
        desenharpessoa(filho, 1440, 350)

def desenharpessoa(pessoa, x, y):
    Olho = Actor('olho_'+pessoa.corolho)
    Olho.pos = (x,y)
    Olho.draw()
    Genero = Actor(pessoa.genero)
    Genero.pos = (x,y)
    Genero.draw()
    Cabelo = Actor(pessoa.genero+'_'+pessoa.tipocabelo+'_'+pessoa.corcabelo)
    Cabelo.pos = (x,y)
    Cabelo.draw()

#criacao do filho
def dedodeDeus(homem, mulher):
    global filho
    if (homem.p_cabelo > mulher.p_cabelo):
        Genero = homem.genero
        Tipocabelo = homem.tipocabelo
        Corcabelo = homem.corcabelo
    if (mulher.p_cabelo >= homem.p_cabelo):
        Genero = mulher.genero
        Tipocabelo = mulher.tipocabelo
        Corcabelo = mulher.corcabelo

    if (homem.p_olho > mulher.p_olho):
        Corolho = homem.corolho
    if (mulher.p_olho >= homem.p_olho):
        Corolho = mulher.corolho

    filho = Pessoa(Genero, Corolho, Tipocabelo, Corcabelo, 0.0, 0.0)
    
def update():
    pass

def on_mouse_down(pos):
    global frame_selecionadoM, frame_selecionadoF, frame_f, frame_m, pessoas_fem, pessoas_masc, filho
    if colisao_m1.collidepoint(pos):
        frame_selecionadoM.pos = (220,341)
        frame_m = 0
    if colisao_m2.collidepoint(pos):
        frame_selecionadoM.pos = (476,341)
        frame_m = 1
    if colisao_m3.collidepoint(pos):
        frame_selecionadoM.pos = (732,341)
        frame_m = 2
    if colisao_m4.collidepoint(pos):
        frame_selecionadoM.pos = (988,341)
        frame_m = 3
    if colisao_f1.collidepoint(pos):
        frame_selecionadoF.pos = (220,626)
        frame_f = 0
    if colisao_f2.collidepoint(pos):
        frame_selecionadoF.pos = (476,626)
        frame_f = 1
    if colisao_f3.collidepoint(pos):
        frame_selecionadoF.pos = (732,626)
        frame_f = 2
    if colisao_f4.collidepoint(pos):
        frame_selecionadoF.pos = (988,626)
        frame_f = 3
    if gerar.collidepoint(pos):
        dedodeDeus(pessoas_masc[frame_m], pessoas_fem[frame_f])
    if reset.collidepoint(pos):
        pessoas_masc = {}
        pessoas_fem = {}
        filho = None
        frame_m = None
        frame_f = None
        frame_selecionadoM.pos = (1000,1000)
        frame_selecionadoF.pos = (1000,1000)
        for i in range(0,4):
            pessoas_masc[i] = PessoaRANDOM('masc')
            pessoas_fem[i] = PessoaRANDOM('fem')
        

pgzrun.go()