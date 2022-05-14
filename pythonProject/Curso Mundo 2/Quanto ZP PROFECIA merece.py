from time import sleep
ZP = True
while ZP < 2:
        ZP = float(input('\033[;1mQuantos ZP o PROFECIA merece ganhar esta semana?\033[m \n'))
        sleep(0.5)
        if ZP >= 1:
                str(input('\n\033[1;35mObrigado pela colaboração semanal!\033[m'))
                break
        if ZP < 1:
                str(input('\033[1;31mPague a taxa semanal de ZP ao PROFECIA\033[m'))
