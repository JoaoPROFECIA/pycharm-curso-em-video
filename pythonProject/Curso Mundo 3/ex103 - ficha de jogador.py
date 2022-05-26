def ficha(jog='<desconhecido>', gol=0):
    '''
    -> Exibe uma ficha de jogador/time
    :param jog: Nome do jogador (str)
    :param gol: Número de gols marcados (str > int)
    :return: Uma ficha de jogador/time
    
    '''

    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')    


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)
