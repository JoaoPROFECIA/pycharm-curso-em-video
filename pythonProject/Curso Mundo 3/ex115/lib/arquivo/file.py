from lib.interface.funcoes import *
import os
import shutil

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        #  mover arquivo para o diretorio atual
        source = r'C:\Users\victo\OneDrive\Documentos\MeuProjetos\pycharm-curso-em-video\pythonProject\curso_mundo_3.txt'
        destination = r'C:\Users\victo\OneDrive\Documentos\MeuProjetos\pycharm-curso-em-video\pythonProject\Curso Mundo 3\ex115\curso_mundo_3.txt'
        shutil.move(source, destination)
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('Erro ao ler arquivo!')
    else:
        cabecalho('Pessoas cadastradas')
        print(a.read())
