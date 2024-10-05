#import tkinter as tk
import selenium 
from selenium import webdriver
import time
from selenium.webdriver.common.by import By



driver = webdriver.Edge(executable_path = r'C:\Users\Desktop\files\msedgedriver.exe')
driver.get("https://www.epssura.com/sitio-medicamentos-poblacion-priorizada")

#encontrar y oprimir el botón de inicio 
btnPedido = driver.find_element(By.XPATH,'//*[@id="content_area"]/div[2]/div/div[2]/section[3]/div[1]/div/div/div[2]/div/a')
btnPedido.click()
time.sleep(2)

#encontrar y oprimir el list item del tipo de documento
lblDocumento = driver.find_element(By.XPATH, '//*[@id="selectTipoDoc"]')
lblDocumento.click()
time.sleep(2)
ccTipo = driver.find_element(By.XPATH, '//*[@id="selectTipoDoc"]/option[2]')
time.sleep(2)
ccTipo.click()

#Encontrar y escribir en el campo del documento
numDocumento = driver.find_element(By.XPATH, '//*[@id="numeroDocumento"]').send_keys("10011015897")
time.sleep(1)

#Encontrar y poner la fecha en el dataPicker
btnCalendar = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/form/div[1]/div[2]/div[1]/div/span/button')
time.sleep(2)
btnCalendar.click()
time.sleep(2)
lblFecha = driver.find_element(By. XPATH, '/html/body/div[1]/div[2]/div/div/form/div[1]/div[2]/div[1]/div/ul/li/div/table/thead/tr/th[1]/button')
time.sleep(1)
lblFecha.click()
time.sleep(1)

#Encontraar y oprimir el botón del día
btnDia = driver.find_element(By. XPATH, '//*[@id="datepicker-765-616-2"]/button/span')
time.sleep(2)
btnDia.click()
