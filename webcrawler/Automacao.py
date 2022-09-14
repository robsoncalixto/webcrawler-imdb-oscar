#import pyautogui
#import time
#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import service

#servico = (ChromeDriveManager().install)
#navegador = webdriver.chrome(service=servico)

#navegador.get("https://www.imdb.com/")
#navegador.find_element('xpath', '//*[@id="iconContext-menu"]/path[2]').click()

#pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código está executando")
#pyautogui.PAUSE = 0.5

#pyautogui.press('winleft')
#time.sleep(2)
#pyautogui.write('google chrome')
#time.sleep(2)
#pyautogui.press('enter')
#time.sleep(5)
#pyautogui.write("https://www.imdb.com/")
#pyautogui.press('enter')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

browser = webdriver.Chrome(service=Service("webcrawler\\driver\\chromedriver.exe") )
browser.get("https://www.imdb.com/oscars/?ref_=nv_ev_acd")
browser.find_element('xpath',"//a[contains(text(),'2022')]").click()