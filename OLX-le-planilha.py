import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import *
import time  
import shutil

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

wb = load_workbook("carga-anuncios-OLX.xlsx")
ws = wb.active

driver = webdriver.Firefox(executable_path="geckodriver/geckodriver-mac")

def iniciaFFlogaOLX():
	driver.get("https://www2.olx.com.br/desapega")
	#time.sleep(5) 
	if(driver.find_element("id", "cookie-notice-ok-button")):
		driver.find_element("id", "cookie-notice-ok-button").click()
	#driver.find_element(By.CLASS_NAME, "sc-iBEsjs").click()
	#login google driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[1]/div[2]/a/span").click()
	#time.sleep(5) 
	#google driver.find_element("xpath", '//*[@id="identifierId"]').send_keys("fmatelli@gmail.com")
	#google driver.find_element("id", "identifierId").send_keys("fmatelli@gmail.com")
	#google driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]").click()
	#driver.switch_to.window(driver.window_handles[1])
	#driver.find_element("id", "email").send_keys("fmatelli@gmail.com")
	#driver.find_element("id", "pass").send_keys("$167F943B")
	driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[1]/div[2]/input').send_keys("fmatelli@gmail.com")
	driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[2]/div[2]/div/div/input').send_keys("$167O943L")	
	driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[1]/div[2]/form/button').click()
	#driver.find_element_by_css_selector('[value="Log In"]').click()
	time.sleep(5) 
	driver.switch_to.window(driver.window_handles[0])
	time.sleep(12)

def clear_entire_text(element):
    element.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)

def preencheOLX(tit, desc, price, CEP):
	#
	clear_entire_text(driver.find_element("id", "subject"))
	driver.find_element("id", "subject").send_keys(tit)
	#
	clear_entire_text(driver.find_element("id", "body"))
	driver.find_element("id", "body").send_keys(tit)
	#with open(os.path.join(sys.path[0], "OLX-rodape-anuncios.txt"), "r") as file:
	#file = open(os.path.join(__location__, "OLX-rodape-anuncios.txt"))
	#driver.find_element("id", "body").send_keys(file.read())
	#
	btn1 = driver.find_element_by_xpath("//*[@id='category_item-7060]")
	driver.execute_script("arguments[0].click();", btn1)
	#
	time.sleep(3)
	driver.find_element_by_css_selector("[aria-label='Informática]").click()
	time.sleep(4)
	#
	clear_entire_text(driver.find_element("id", "price_text"))
	driver.find_element("id", "price_text").send_keys(price)
	#
	clear_entire_text(driver.find_element("id", "zipcode"))
	driver.find_element("id", "zipcode").send_keys(CEP)
	time.sleep(2)

def uploadImage(path):
	files = driver.find_element_by_css_selector("[type='file']")
	files.send_keys(path)
	print("Cadastrando imagem, aguarde...")
	time.sleep(3)

def submitForm():
	askContinue("Imagens carregaram. Reveja anuncio, tudo pronto para enviar?")
	driver.find_element_by_xpath("//*[@id='ad_insertion_submit_button]").click()
	time.sleep(10)
	driver.get("https://www2.olx.com.br/desapega")

def askContinue(what):
	answer = input(what)
	if answer.lower() in ["n","no"]:
	    exit 

iniciaFFlogaOLX()

for row in ws.iter_rows(min_row=2, max_col=20):
	if row[1].value:
		#print("CEP: "+row[0].value.strip()+" \nTitulo: "+row[1].value.strip()+"\nDesc: "+row[2].value.strip()+"\nCat: "+row[3].value.strip()+"\nSub-cat: "+row[4].value.strip()+" \nPreco: ")
		#print(row[5].value);
		#preencheOLX(tit 1 , desc 2, price 3, CEP 0);
		preencheOLX(row[1].value.strip(), row[2].value.strip(), row[5].value, row[0].value.strip())