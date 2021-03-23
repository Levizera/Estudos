# Problemas --> Resolver a questão de receber 3 argumentos
# Saber qual será implementado na função
# Arrumar jeito de deixar apenas 1 argumento sem quebrar o codigo

import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
import shutil

class File_manager:
    def __init__(self, dir_name, file_name, dest_path):
        self.dir_name = dir_name
        self.file_name = file_name
        self.dest_path = dest_path
        
    def new_dir(self):
        dir = self.dir_name
        os.mkdir(dir)
    
    def delete_dir(self):
        dir = self.dir_name
        os.rmdir(dir)
    
    def new_file(self):
        file = self.file_name
        Path(file).touch()
    
    def delete_file(self):
        file = self.file_name
        os.remove(file)
    
    def list_files(self):
        path = self.dest_path
        files = [f for f in listdir(path) if isfile(join(path, f))]
        print(files)
        
    def move_files(self):
        file = self.file_name
        path = self.dest_path
        shutil.move(file, path)
    
    def copy_file(self):
        file = self.file_name
        path = self.dest_path
        shutil.copy(file, path)
    
    
# new_directory takes 3 arguments but only one is used
# 1. Dir name 2. File name 3. Path 
file_manager = File_manager('', '', '')