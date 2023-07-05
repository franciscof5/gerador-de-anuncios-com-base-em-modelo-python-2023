#2022-08-01
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from openpyxl import *
import time  
import shutil

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
pathi = __location__

driver = webdriver.Firefox(executable_path="/home/francisco/geckodriver/geckodriver")
driver.get("https://www.instagram.com/")
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys("lojasdomago.com.br")
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys("$167I943N")
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click()
time.sleep(5) 
driver.get("https://www.instagram.com/")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button').click()
def clear_entire_text(element):
    element.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

def publicarPostInstagram(tit, desc, price, CEP):
	#
	clear_entire_text(driver.find_element_by_css_selector('#subject'))
	driver.find_element_by_css_selector('#subject').send_keys(tit)
	#
	clear_entire_text(driver.find_element_by_css_selector('#body'))
	driver.find_element_by_css_selector('#body').send_keys(tit)
	#with open(os.path.join(sys.path[0], "OLX-rodape-anuncios.txt"), "r") as file:
	file = open(os.path.join(__location__, 'OLX-rodape-anuncios.txt'))
	driver.find_element_by_css_selector('#body').send_keys(file.read())
	#
	btn1 = driver.find_element_by_xpath('//*[@id="category_item-5000"]')
	driver.execute_script("arguments[0].click();", btn1)
	#
	time.sleep(3)
	btn2 = driver.find_element_by_xpath('//*[@id="category_item-5020"]')
	driver.execute_script("arguments[0].click();", btn2)
	time.sleep(4)
	#
	clear_entire_text(driver.find_element_by_css_selector('#price_text'))
	driver.find_element_by_css_selector('#price_text').send_keys(price)
	#
	clear_entire_text(driver.find_element_by_css_selector('#zipcode'))
	driver.find_element_by_css_selector('#zipcode').send_keys(CEP)
	time.sleep(2)
	
def uploadImage(path):
	files = driver.find_element_by_css_selector("[type='file']")
	files.send_keys(path)
	print("Cadastrando imagem, aguarde...")
	time.sleep(3)

def submitForm():
	askContinue("Imagens carregaram. Reveja anuncio, tudo pronto para enviar?")
	driver.find_element_by_xpath('//*[@id="ad_insertion_submit_button"]').click()
	time.sleep(10)
	driver.get("https://www2.olx.com.br/desapega")

def askContinue(what):
	answer = input(what)
	if answer.lower() in ["n","no"]:
	    exit 

#time.sleep(12)
print("VARRENDO: " + pathi + "/anuncios-prontos")
os.chdir(pathi + "/anuncios-prontos")
for dirpath, dirname, filenames in os.walk("."):
    if os.path.isdir(dirpath) and dirpath != "." and dirpath != "svgs":
        print("Cadastrando produto: " + dirpath[2:])
        index = 1;
        for filename in filenames:
            if(index == 1):
            	#tit, desc, price, CEP
            	#preencheOLX(dirpath[2:-5], dirpath[2:-5],dirpath[-4:], "18201-608")
            	print("primeira img:" + dirpath[2:-5])
            #img filepath
            #if(index <= 6):
	        #    uploadImage((pathi + dirpath[2:] + "/" + filename))
            index += 1;
        #submitForm()
        print("movendo diretorio do produto para ../carga-anuncios-OLX-feito/")
        
        #####shutil.move(dirpath, "../carga-anuncios-OLX-feito/")
        #askContinue("O diretório foi movido corretamente?")
            #os.chdir("..")
    print("PRODUTO CADASTRADO COM SUCESSO: " + dirpath[2:-5])
    askContinue("Procurar próxima pasta com fotos de produto?")

#driver.find_element_by