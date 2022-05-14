while 1:
    import pygame
    print('\nTOCANDO UM MP3\n')
    print('''Escolha um som: 
    1 - Eu acho que é melhor ficarmos aqui!
    2 - Todo mundo junto, mas eu fico por ultimo pra não morrer!
    3 - Aqui não vai sobrar nenhuma bala no pente!
    4 - Sair''')
    opcao = int(input('\nDigite um número: '))
    if opcao == 1:
        pygame.mixer.init()
        pygame.mixer.music.load('ex021a.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        input('\nPressione Enter para continuar')
    if opcao == 2:
        pygame.mixer.init()
        pygame.mixer.music.load('ex021b.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        input('\nPressione Enter para continuar')
    if opcao == 3:
        pygame.mixer.init()
        pygame.mixer.music.load('ex021c.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        input('\nPressione Enter para continuar')
    if opcao == 4:
        break
