import os
from string import digits


def rename_files():
    file_list = os.listdir("pics")
    print(file_list)
    
    save_path = os.getcwd()
    os.chdir(save_path+"\pics")
    
    for file_name in file_list:
        os.rename(file_name, file_name.translate(str.maketrans('', '', digits)))
        
    os.chdir(save_path)
    
rename_files()
