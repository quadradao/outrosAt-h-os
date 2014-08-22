# outrosAt(h)os_01-painel.py
# 1. instruções:
# 2.    tecle(cmd+a)
# 3.    tecle(cmd+c)
# 4.    abra(drawbot):
# 5.        tecle(cmd+v)
# 6.        tecle(cmd+r)
# 7.        se quiser ver denovo:
# 8.            tecle(cmd+r)
# 7.            enquanto quiser ver denovo:
# 8.                tecle(cmd+r)
# 9.        caso contrário:
# 10.           feche(drawbot)

autor = objeto = local = data = dimensoes = arquiteto = ''

#  agi são paulo 2014
##  special project
###  desenvolvido por quadradão_qdd.qlb
####  que quer comer a fruta inteira
#####  à convite de guto lacaz        
######  os outros at(h)os = (x)bulcão 
#######  painel de azulejos do museu de gemas
########  dois motivos

##########  dados

museuDeGemas = {
    autor :
        'athos bulcão',
    objeto : 
        'painel de azulejos',
    local : 
        ['museu de gemas', {arquiteto : 'lúcio costa'}, 'torre de tv', 'brasília', 'df', 'brasil'],
    data : 
        1966,
    dimensoes : 
        (1295, 353), #  em centímetros
    }

#########################  motivos

def motivo_triangulo_azul( ):
    '''
    ###########|#          |###########|          #
    #########  |###        |  #########|        ###
    #######    |#####      |    #######|      #####
    #####      |#######    |      #####|    #######
    ###        |#########  |        ###|  #########
    #          |###########|          #|###########
    '''
    save()
    translate(lado/2, lado/2)
    n = randint(0,3) ##############  escolhe posição do motivo
    rotate(n*90) ###################  rotaciona para a posição escolhida
    stroke(None)
    fill(0, 0, 1) ####################  colore de azul
    translate(-lado/2, -lado/2)
    polygon((0,0), (0, lado), (lado, 0), (0,0))
    #####################################  desenha o triângulo
    restore()

def motivo_linha_azul( ):
    '''
        ###    |           |           |    ###
        ###    |           |           |    ###
        ###    |###########|###########|    ###
        ###    |###########|###########|    ###
        ###    |           |           |    ###
        ###    |           |           |    ###
    '''
    save()
    translate(lado/2, lado/2)
    n = randint(0,1) ###############################  escolhe posição do motivo
    rotate(n*90) ####################################  rotaciona para a posição escolhida
    stroke(None)
    fill(0, 0, 1) #####################################  colore de azul
    translate(-lado/2, -lado/10)
    rect(0,0, lado, lado/5) #############################  desenha a linha
    restore()

############################################################  variáveis

size(museuDeGemas[dimensoes]) ################################  define as dimensões do painel infinito a partir dos dados
lado = 20 #####################################################  define as dimensões do motivo quadrado
horizontal = int(width()/lado)+1 ###############################  calcula quantos motivos cabem na largura do painel
vertical = int(height()/lado)+1 #################################  calcula quantos motivos cabem na altura do painel

###################################################################  painel

for motivo in range(vertical): ######################################  cria o painel
    save()
    for motivo in range(horizontal): ##################################  pra cada posição
        n = randint(0,1) ###############################################  escolhe um motivo e desenha
        if n == 0:
            motivo_triangulo_azul( )
        else:
            motivo_linha_azul( )
        translate(lado, 0)
    restore()
    translate(0, lado) ########################################################  repete
