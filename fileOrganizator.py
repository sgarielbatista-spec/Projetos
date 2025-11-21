import os
import shutil

def creat_a_folder_on_the_desktop(nome): #recebe um nome e cria uma pasta
    desktop = os.path.join(r"C:\Users\silva\OneDrive\Desktop\folder_organizator", nome) #cria um endereço
    os.makedirs(desktop, exist_ok=True) #cria a pasta no endereço passado.
    return desktop #retorna o endereço criado

directory_download  = os.path.join(os.path.expanduser("~"), "Downloads") #endereço da pasta Downloads

for item in os.listdir(directory_download): #Itera sobre todos os itens da pasta
    file_path = os.path.join(directory_download, item) #cria o endereço exato de cada arquivo
    name, ext = os.path.splitext(item) #separa o nome do arquivo do nome da extensão

    if os.path.isfile(file_path): #verifica se é pasta ou arquivo
        destination_folder = creat_a_folder_on_the_desktop(ext.replace(".", "")) #passa o nome da extensão sem o ponto para a função, e retorna o endereço da nova pasta
        shutil.move(file_path, destination_folder) #endereço de onde esta o arquivo e o seu destino.
        