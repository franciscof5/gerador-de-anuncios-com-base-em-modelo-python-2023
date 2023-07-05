#Funcionamento
#Uma pasta pai é indicada
#Cada pasta filho é o Título, Preço, +
#Uma pasta pai é indicada
#Cada pasta filho é o Título (separado por 4 espaços Preço
#todo: Cada foto dentro compõem um mosaico dos produtos
#A primeira foto é de destaque
#O título do anuncio aparece na imagem final
#A data do anúncio aparece na imagem final
#O preço do anúncio aparece na imagem final (após primeira vírgula)
#Se tiver um arquivo logo.png ele é chumbado no anúncio

#!/usr/bin/python3
# import the modules
import os
from os import listdir
import pathlib
import sys
import subprocess
import shlex

pathlib.Path.cwd()
# get the path/directory
#folder_dir = pathlib.Path.cwd()#"imgs"
folder_dir = "gerar-anuncios/1345 Caixa Estanque Gopro Hero 5 6 7 Black Tampa Touch Go Pro"

#for images in os.listdir(folder_dir):
#    print(images)

def geraThumbSVG(replace_numero, replace_titulo, pathi, dirpath, filename):
    #pass
    # check if the image ends with png
    #if (images.endswith(".jpg")):
        original_stdout = sys.stdout 
        #with open(images+'.svg', 'w') as f:
        
        #replace_numero = folder_dir[15:19]
        #print(replace_numero)
        #replace_titulo = folder_dir[17:-4]
        #replace_imagem = "/media/francisco/Files/Dropbox/python-classificados/gerar-anuncios/1345 Caixa Estanque Gopro Hero 5 6 7 Black Tampa Touch Go Pro/"+images
        #print(replace_imagem)
        
        #print(numero + titulo + imagem)
        # creating a variable and storing the text
        # that we want to search
        search_numero = "TROCARNUMERO"
        search_titulo = "TROCARTITULO"
        search_imagem = "TROCARIMAGEM"
        # creating a variable and storing the text
        # that we want to add
        #replace_text = "replaced"
          
        # Opening our text file in read only
        # mode using the open() function
        #with open(r'/media/francisco/Files/Dropbox/python-classificados/gerar-anuncios/modelo-anuncio.svg', 'r') as file:
        
        ###PEGAR TAMANHO DA IMAGEM E ESCOLHER MODELO CERTO?
        with open(r'modelo-anuncio-samsung.svg', 'r') as file:
        
            # Reading the content of the file
            # using the read() function and storing
            # them in a new variable
            data = file.read()
          
            # Searching and replacing the text
            # using the replace() function
            data = data.replace(search_titulo, replace_titulo[:-4])
            data = data.replace(search_numero, replace_numero)
            #print("FOI " + pathi + "svgs/../" + dirpath + filename); 
            data = data.replace(search_imagem, pathi + dirpath + "/" + filename)
          
        # Opening our text file in write only
        # mode to write the replaced content
        #with open("/media/francisco/Files/Dropbox/python-classificados/gerar-anuncios/svgs/"+replace_titulo[:-4]+'.svg', 'w') as file:
        print("svgs/" + replace_titulo[:-4] + ".svg")
	#as
        with open("svgs/" + replace_titulo[:-4] + '.svg', 'w') as file:
        #sys.stdout = f # Change the standard output to the file we created.
        #with open(images+'.svg', 'w') as f:
            # Writing the replaced data in our
            # text file
            file.write(data)
        
        sys.stdout = original_stdout # Reset the standard output to its original value

        #print(images)
        ##/mnt/24860678-791e-4d8d-ab99-c76390855d86/Dropbox/vamoslonge-thumbs/thumbmaker-relatos-viajados/043 Salvador.jpg

pathi = os.path.dirname(os.path.realpath(__file__)) + "/gerar-anuncios/"
#pathi = '/home/francisco/Dropbox/2022-OLX-republicador/gerar-anuncios/'
#pathi = 'gerar-anuncios/'

#cd path
os.chdir(pathi)
for dirpath, dirname, filenames in os.walk("."):
    if os.path.isdir(dirpath) and dirpath != "." and dirpath != "svgs":
        #print("d" + dirpath)
        #print("H" + dirpath)
        #os.chdir(dirpath)
        index = 1;
        print(filenames)
        for filename in filenames:
            #print("img" + os.path.join(dirpath,filename) + " index: " + str(index) )
            if(index == 1):
                print("NUM: " + dirpath[-4:] + " TIT: " + dirpath[2:] + " FIL: " + (pathi + dirpath[2:] + filename) )
                #replace_numero, replace_titulo, pathi, dirpath, filename)
                geraThumbSVG(dirpath[-4:], dirpath[2:], pathi, dirpath[2:], filename)
            index += 1;

            #os.chdir("..")
    print("-------")

#os.system("sh svg-to-png.sh")
#os.system('svg-to-png.sh')
#os.system('./svg-to-png.sh')
#subprocess.call(['sh', './svg-to-png.sh'])
#subprocess.call(shlex.split("./svg-to-png.sh"))
