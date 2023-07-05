#Funcionamento
#Uma pasta pai é indicada
#Cada pasta filho é o Título (separado por 4 espaços Preço
##A desenvolver: cadastra na OLX e Facebook (ou pré-cadastra)
## CADASTRAR NA LOJA VIRTUAL PROPRIA
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from openpyxl import *
import time  
import shutil

pathi = '/media/francisco/Files/Dropbox/python-classificados/carga-anuncios-OLX/'
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
#import pyodbc
#import unidecode

#wb = load_workbook('carga-anuncios-OLX.xlsx')
#for row in ws.iter_rows(min_row=1, max_col=20, max_row=131):
#	if row[1].value:
#		print('-- INSERE OBRA: '+row[1].value.strip())

driver = webdriver.Firefox(executable_path="/home/francisco/geckodriver/geckodriver")
driver.get("https://www2.olx.com.br/desapega")
#driver.find_element_by_css_selector('[type="email"]').send_keys("fmatelli@gmail.com")
#driver.find_element_by_css_selector('[type="password"]').send_keys("$167O943L")
#driver.find_element_by_xpath("//form/button").submit()
driver.find_element("id", "cookie-notice-ok-button").click()
driver.find_element_by_css_selector('.sc-iBEsjs').click()

time.sleep(5) 

driver.switch_to.window(driver.window_handles[1])

driver.find_element_by_css_selector('#email').send_keys("fmatelli@gmail.com")
driver.find_element_by_css_selector('#pass').send_keys("$167F943B")
driver.find_element_by_css_selector('[value="Log In"]').click()

#driver.find_element_by_xpath("//form/button").submit()

time.sleep(5) 
driver.switch_to.window(driver.window_handles[0])


#def (titulo, desc, cat, subcat, price, CEP):
#	print("inicio")
	#subject
	#body
	#click category_item-5000 #category_item-5020
	#price_text
	#type="file"
	#zipcode
def clear_entire_text(element):
    element.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

def preencheOLX(tit, desc, price, CEP):
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
	#type="checkbox"
	askContinue("Imagens carregaram. Reveja anuncio, tudo pronto para enviar?")
	driver.find_element_by_xpath('//*[@id="ad_insertion_submit_button"]').click()
	time.sleep(10)

	#button data-testid="main-button-confirmation-dialog"
	#driver.find_element_by_css_selector('data-testid="main-button-confirmation-dialog"').click()
	#askContinue("inserir próximo?")
	driver.get("https://www2.olx.com.br/desapega")
	#sc-keVrkP https://www3.olx.com.br/account/userads (opcional)

def askContinue(what):
	answer = input(what)
	if answer.lower() in ["n","no"]:
	    exit 

time.sleep(12)
#askContinue("A página de cadastrar já terminou de carregar?")
#cd path
os.chdir(pathi)
for dirpath, dirname, filenames in os.walk("."):
    if os.path.isdir(dirpath) and dirpath != "." and dirpath != "svgs":
        #print("d" + dirpath)
        print("Cadastrando produto: " + dirpath[2:])
        #os.chdir(dirpath)
        index = 1;
        for filename in filenames:
            if(index == 1):
            	#tit, desc, price, CEP
            	preencheOLX(dirpath[2:-5], dirpath[2:-5],dirpath[-4:], "18201-608")
            #img filepath
            if(index <= 6):
	            uploadImage((pathi + dirpath[2:] + "/" + filename))
            index += 1;
        submitForm()
        print("movendo diretorio do produto para ../carga-anuncios-OLX-feito/")
        shutil.move(dirpath, "../carga-anuncios-OLX-feito/")
        #askContinue("O diretório foi movido corretamente?")
            #os.chdir("..")
    print("PRODUTO CADASTRADO COM SUCESSO: " + dirpath[2:-5])
    askContinue("Procurar próxima pasta com fotos de produto?")

#driver.find_element_by