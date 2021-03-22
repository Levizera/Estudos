import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
import shutil

# Funções de um gerenciador
# --> Mostrar os arquivos XX
# --> Criar Pastas XX
# --> Apagar Pastas XX
# --> Criar novos arquivos XX
# --> Apagar arquivos XX
# --> Mover arquivos XX 
# --> Copiar arquivos XX



# Cria Diretorios
def criar_diretorio():
    nome_do_dir = input('Insira o nome do diretório que deseja criar: ')
    dir = nome_do_dir
    os.mkdir(dir)

# Apaga diretorios
def apagar_dir():
    nome_do_dir = input('Insira o nome do diretorio que deseja apagar: ')
    os.rmdir(nome_do_dir)

# Cria novos arquivos
def criar_arquivos():
    nome_do_arquivo = input('Insira o nome do arquivo: ')
    Path(nome_do_arquivo).touch()
    
    
# Apaga arquivos
def apagar_arquivos():
    nome_do_arquivo = input('Insira o nome do arquivo que deseja apagar: ')
    remover_arq = os.remove(nome_do_arquivo)
    
# Lista arquivos
def listar_arquivos():
    nome_do_dir = input('Insira o path do diretório que deseja ver os arquivos: ')
    path = nome_do_dir
    files = [f for f in listdir(path) if isfile(join(path, f))]
    print(files)

# Mover arquivos 
def mover_arquivos():
    nome_file_dir = input('Insira o nome do arquivo/diretorio que voce deseja mover: ')
    destino = input('Insira o path para qual o seu arquivo/diretorio vai ser movido: ')
    shutil.move(nome_file_dir, destino)


# Copiar arquivos 
def copiar_arquivos():
    src = input('Qual o nome do seu arquivo? ')
    des = input(f'Qual o nome do diretorio que deseja enviar a copia do {src}? ')
    shutil.copy(src, des)
    
criar_diretorio()
criar_arquivos()
copiar_arquivos()


