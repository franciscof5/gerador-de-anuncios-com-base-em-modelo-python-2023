#encoding: utf-8
#Funcionamento

#Uma pasta pai é indicada
#Cada pasta filho é o Título, Preço, +

import os
from os import listdir
import sys
import subprocess
import shlex
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from cairosvg import svg2pdf
from distutils.dir_util import copy_tree
import shutil

path_execucao_script = os.path.dirname(os.path.realpath(__file__)) + "/"

## SETTINGS MANAGER ##

#absoluto no sistema (precisa / no final)
path_anuncios = "/Users/francisco/Downloads/anuncios-controle/usados/"

#modelo do anuncio atual
modelo_anuncio = "lojasdomago-instagram"
modelo_os = "-macos"
path_execucao_script_modelo_anuncio = path_execucao_script+'modelos-de-anuncios/' + modelo_anuncio + '/'
path_execucao_script_anuncios_prontos = path_execucao_script + "anuncios-prontos/" + modelo_anuncio + "/"

#Precisa remover tudo, porque é gerado com Nome  e preço no final, e quando vender tem que sair
if os.path.isdir(path_execucao_script_anuncios_prontos):
    shutil.rmtree(path_execucao_script_anuncios_prontos)

#Depois de apagar, recria
os.mkdir(path_execucao_script_anuncios_prontos) 

#Dropbox folder
path_dropbox = "/Users/francisco/Dropbox/"


def geraThumbSVG(novo_preco, novo_titulo, path_scaneado, file_relative_path, filename):
    original_stdout = sys.stdout 
    search_preco = "TROCARNUMERO"
    search_titulo = "TROCARTITULO"
    search_imagem = "TROCARIMAGEM"
    
    svg_gerado = path_execucao_script_modelo_anuncio + "svgs/" + novo_titulo + ".svg"
    novo_imagem_bg = path_scaneado + file_relative_path + "/" + filename
    print(" \n geraThumbSVG(), svg_gerado: " + svg_gerado + " \n novo_imagem_bg: " + novo_imagem_bg)
    novo_preco = novo_preco.replace("$", "").replace("R", "")
    ###PEGAR TAMANHO DA IMAGEM E ESCOLHER MODELO CERTO?
    with open(path_execucao_script_modelo_anuncio + modelo_anuncio + modelo_os + '.svg', 'rt') as file:
        data = file.read()
        data = data.replace(search_titulo, novo_titulo)
        data = data.replace(search_preco, novo_preco)
        data = data.replace(search_imagem, novo_imagem_bg)
        #data = data.replace("R$", "")

    with open(svg_gerado, 'w', encoding='utf-8') as file:
        file.write(data)

    #
    salvar_imagem_na_pasta_de_anuncio = path_scaneado + file_relative_path + "/_anuncio-" + novo_preco + "-" + novo_titulo + ".jpg"
    salvar_imagem_na_pasta_do_script = path_execucao_script + "anuncios-prontos/" + modelo_anuncio + "/" + novo_titulo + ".jpg"
    #
    drawing = svg2rlg(svg_gerado)
    #
    renderPM.drawToFile(drawing, salvar_imagem_na_pasta_de_anuncio, fmt="JPG")
    renderPM.drawToFile(drawing, salvar_imagem_na_pasta_do_script, fmt="JPG")
    print (" \n salvar_imagem_na_pasta_de_anuncio: " + salvar_imagem_na_pasta_de_anuncio)
    print (" \n salvar_imagem_na_pasta_do_script: " + salvar_imagem_na_pasta_do_script)
    print (" ####### \n")
    
    sys.stdout = original_stdout # Reset the standard output to its original value

def scanDir(path_scaneado):
    print("scanDir(): " + path_scaneado)
    os.chdir(path_scaneado)
    for dirpath, dirname, filenames in os.walk("."):
        if os.path.isdir(dirpath) and dirpath != "." and dirpath != "svgs":
            index = 1;
            print("Array de arquivos indexas no diretório: ")
            print(sorted(filenames, reverse=True))
            for filename in sorted(filenames, reverse=True):
                if(  filename[0:9] == "_anuncio-" ):
                    print("Encontrado thumbnail renderizada (já com preço), buscando próxima imagem para geraThumbSVG()")
                    #os.remove(path_scaneado+dirpath+"/"+filename)
                else:
                    if( filename != ".DS_Store" and 
                        filename.lower().endswith(('.jpg')) and not 
                        filename.lower().endswith(('lowquality.jpg')) ):
                        if(index == 1):
                            file_preco = dirpath[-4:]
                            file_titulo =  os.path.basename(dirpath[2:])
                            file_relative_path = dirpath
                            file_path = (path_scaneado + dirpath[2:] + filename)
                            print("\n Preço: " + file_preco + " \n Titulo: " + file_titulo + " \n Caminho: " + file_path + " \n filename: " + filename + " \n")
                            geraThumbSVG(file_preco, file_titulo, path_scaneado, file_relative_path, filename)
                        index += 1;
        print("------- pasta finalizada, próxima --------")
    print("------ Script executado com sucesso, arquivos gerados ------")
    copyFolderToDropbox()

def copyFolderToDropbox():
    path_dropbox_anuncios_prontos = path_dropbox + "anucios-prontos/" + modelo_anuncio
    #
    if os.path.isdir(path_dropbox_anuncios_prontos):
        shutil.rmtree(path_dropbox_anuncios_prontos)
    #
    copy_tree(path_execucao_script_anuncios_prontos, path_dropbox_anuncios_prontos)

scanDir(path_anuncios)

