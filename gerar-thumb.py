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
#import cairosvg
#import weasyprint
#import cairo
#import rsvg
#import pyvips
#from potrace import Bitmap

#relativo ao diretório atual, um filho
path_anuncios = os.path.dirname(os.path.realpath(__file__)) + "/gerar-anuncios/"

current_path = os.path.dirname(os.path.realpath(__file__)) + "/"

#absoluto no sistema (precisa / no final)
path_anuncios = "/Users/francisco/Downloads/anuncios-controle/usados/"

def geraThumbSVG(replace_numero, replace_titulo, pathi, file_relative_path, filename):
    original_stdout = sys.stdout 
    search_numero = "TROCARNUMERO"
    search_titulo = "TROCARTITULO"
    search_imagem = "TROCARIMAGEM"
    
    svg_gerado = current_path+"modelos-de-anuncios/svgs/" + replace_titulo + ".svg"
    svg_imagem = pathi + file_relative_path + "/" + filename
    print(" \n geraThumbSVG(), svg_gerado: " + svg_gerado + " \n svg_imagem: " + svg_imagem)

    ###PEGAR TAMANHO DA IMAGEM E ESCOLHER MODELO CERTO?
    with open(current_path+'modelos-de-anuncios/modelo-anuncio-samsung.svg', 'r') as file:
        data = file.read()
        data = data.replace(search_titulo, replace_titulo)
        data = data.replace(search_numero, replace_numero)
        data = data.replace(search_imagem, svg_imagem)
    
    

    with open(svg_gerado, 'w') as file:
        file.write(data)

    drawing = svg2rlg(svg_gerado)
    renderPDF.drawToFile(drawing, "file.pdf")
    renderPM.drawToFile(drawing, current_path + "anuncios-prontos/" + replace_titulo[:-4] + ".jpg", fmt="JPG")

    sys.stdout = original_stdout # Reset the standard output to its original value

def scanDir(pathi):
    print("scanDir(): " + pathi)
    os.chdir(pathi)
    for dirpath, dirname, filenames in os.walk("."):
        if os.path.isdir(dirpath) and dirpath != "." and dirpath != "svgs":
            index = 1;
            print("Array de arquivos indexas no diretório: ")
            print(sorted(filenames))
            for filename in sorted(filenames):
                if(filename != ".DS_Store"):
                    if(index == 1):
                        file_preco = dirpath[-4:]
                        file_titulo =  os.path.basename(dirpath[2:])
                        file_relative_path = dirpath
                        file_path = (pathi + dirpath[2:] + filename)
                        print("\n Preço: " + file_preco + " \n Titulo: " + file_titulo + " \n Caminho: " + file_path + " \n filename: " + filename + " \n")
                        geraThumbSVG(file_preco, file_titulo, pathi, file_relative_path, filename)
                    index += 1;
        print("------- pasta finalizada, próxima --------")

scanDir(path_anuncios)
#os.system("sh svg-to-png.sh")
#os.system('svg-to-png.sh')
#os.system('./svg-to-png.sh')
#subprocess.call(['sh', './svg-to-png.sh'])
#subprocess.call(shlex.split("./svg-to-png.sh"))
