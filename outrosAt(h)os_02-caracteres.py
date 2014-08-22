# outrosAt(h)os_02-caracteres.py
# 1. modo de usar:
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

# dados

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
        (1295, 353), # em centímetros
    }
#  motivos

def modulo_triangulo_azul( ):
    '''
    ###########|#          |###########|          #
    #########  |###        |  #########|        ###
    #######    |#####      |    #######|      #####
    #####      |#######    |      #####|    #######
    ###        |#########  |        ###|  #########
    #          |###########|          #|###########
   '''
    alinhamento = choice(('left', 'right'))
    modulo = ''
    escolhe = randint(0, 1)
    max = 11
    min = 1
    X = "'"
    if escolhe:
        n = max
        for i in range(linhas):
            if alinhamento == 'left':
                linha = n*'#' + (max-n)*X
            else:
                linha = (max-n)*X + n*'#'
            n -= 2
            modulo += linha + '\n'
    else:
        n = min
        for i in range(linhas):
            if alinhamento == 'left':
                linha = n*'#' + (max-n)*X
            else:
                linha = (max-n)*X + n*'#'
            n += 2
            modulo += linha + '\n'
    textBox(modulo, (0, 0, lado, lado), align='center')
    

def modulo_linha_azul( ):
    '''
        ###    |           |           |    ###
        ###    |           |           |    ###
        ###    |###########|###########|    ###
        ###    |###########|###########|    ###
        ###    |           |           |    ###
        ###    |           |           |    ###
    '''
    modulo = ''
    escolhe = randint(0, 1)
    max = 11
    min = 3
    X = "'"
    if escolhe:
        for i in range(linhas):
            if i == 2 or i == 3:
                linha = max*'#'
            else:
                linha = max*X
            modulo += linha + '\n'
    else:
        for i in range(linhas):
            linha = 4*X + min*'#' + 4*X
            modulo += linha + '\n'
    textBox(modulo, (0, 0, lado, lado), align='center')

# variáveis

# for fonte in installedFonts():
#     print fonte
font('Courier')
txt = '############'
lado = textSize(txt)[0]
linha = 10 # n módulos na largura do painel
coluna = 20 # n módulos na altura do painel
size(linha*lado, coluna*lado)
linhas = 6
# lineHeight(lado/len(txt)*2)

# painel

for modulo in range(coluna):
    save()
    for modulo in range(linha):
        n = randint(0,1) # escolhe entre os dois módulos e desenha
        if n:
            # fill(random())
            modulo_triangulo_azul( )
        else:
            # fill(random())
            modulo_linha_azul( )
        translate(lado, 0)
    restore()
    translate(0, lado)

# saveImage('(x)bulcao.pdf')

