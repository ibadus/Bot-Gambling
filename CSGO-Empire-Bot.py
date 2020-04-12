import keyboard
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
import datetime

# Fonctions
def TERRO(browser,mise,i,retrait,start,timer,bmise):
    while i < retrait :
        balance = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/div/div[3]/div[2]/div[3]/div/div/span/span").text
        print("Vous avez {} dans votre balance".format(balance))
        time = True
        while time :
            timer = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[3]/div[2]/div/div[2]").text
            if str(timer) != "15,00":
                time = False
            elif str(timer) != "15,01":
                time = False
            elif str(timer) != "15,02":
                time = False
            print(timer)
        print("===========================")
        print("Betting...")
        print("===========================")
        bet = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[5]/div/div[1]/input")
        bet.send_keys(Keys.CONTROL + "a")
        bet.send_keys(Keys.DELETE)
        mise = str(mise)
        bet.send_keys(mise) #bet de la mise
        print("2s...")
        browser.implicitly_wait(2)
        cote = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[6]/div[3]/div/div/button/div/div[1]/div/span")
        cote.click()
        print("===========================")
        print("Bet fait ! ")
        print("===========================")
        print("En attenete de la nouvelle partie...")
        print("===========================")
        browser.implicitly_wait(12)
        start = ""
        while str(start) != "0,00":
            start = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[7]/div[3]/div/div[1]/div[2]/span").text
        newbalance = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/div/div[3]/div[2]/div[3]/div/div/span/span").text
        if newbalance > balance :
            mise = bmise
            print("W")
        elif newbalance < balance :
            mise = float(mise)
            mise = mise * 2
            i = i + 1
            print("L")
        else :
            browser.implicitly_wait(6)
            newbalance = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/div/div[3]/div[2]/div[3]/div/div/span/span").text
            print("Else")
            if newbalance > balance :
                mise = bmise
                print("W")
            elif newbalance < balance :
                mise = float(mise)
                mise = mise * 2
                i = i + 1
                print("L")
        print("===========================")
        print("Nouvelle mise = {}".format(mise))
        print("===========================")
        print("Nouvelle partie")
        print("===========================")
        balance = newbalance

# Inputs
bmise = ##################################### A CHANGER #####################################
couleur = "TERRO"
retrait = ##################################### A CHANGER ##################################### 

# Variables
url = "https://csgoempire.com/"
mise = bmise
i = 0
timer = "1"
start = 1
a = True

# Début du programme
    # Ouverture du navigateur
        # Option = ouvrir le browser sur l'utilisateur actuel
chrome_options = Options()
chrome_options.add_argument('--user-data-dir=C:\\Users\\Oddon\\AppData\\Local\Google\\Chrome\\User Data') ##################################### A CHANGER ##################################### 
capabilities = DesiredCapabilities.CHROME.copy()
chromedriver = "C:\\Users\\Oddon\\chromedriver.exe" ##################################### A CHANGER ##################################### 
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options = chrome_options, desired_capabilities=capabilities) # Ouverture de Chrome
browser.get(url) # Ouvre l'URL

print("Vous avez choisis {} comme mise de base qui sera *2 lorsque vous perderez.\nLe bot s'arrêtera lorsque vous aurez fait {} défaites de suites.\nVous miserez uniquement sur le côté {}.".format(bmise,retrait,couleur))
print("===========================\n'ESC' pour LANCER le bot sur Chrome.\n===========================")
while a :
    if keyboard.read_key() == 'esc':
        a = False
        TERRO(browser,mise,i,retrait,start,timer,bmise)
    #if keyboard.read_key() == 'esc':
        # Lancement du programme 
        #browser.implicitly_wait(5) # Browser attends 5 secondes
        #pin = browser.find_element_by_xpath("/html/body/div[@id='app']/div[@class='site-layout']/div[@class='site-layout__main relative z-10']/div[@class='page-layout relative z-10']/div[@id='page-scroll']/div[@class='page-layout__inner']/section[@class='w-full']/div[@class='page']/div[@class='page__inner w-full mx-auto pt-8 lg:pt-12 pb-8']/div[@class='bet-input lg:flex lg:justify-center mb-4 lg:mb-5']/div[@class='lg:inline-flex']/div[@class='bet-input__field relative']/div[@class='bet-input__pin']/div/div[@class='input-form mx-auto']/div[@class='relative']/input[@class='security-prompt--roulette']")
        #pin.send_keys(userpin) # Brwoser entre le PIN
        #confirm = browser.find_element_by_xpath("/html/body/div[@id='app']/div[@class='site-layout']/div[@class='site-layout__main relative z-10']/div[@class='page-layout relative z-10']/div[@id='page-scroll']/div[@class='page-layout__inner']/section[@class='w-full']/div[@class='page']/div[@class='page__inner w-full mx-auto pt-8 lg:pt-12 pb-8']/div[@class='bet-input lg:flex lg:justify-center mb-4 lg:mb-5']/div[@class='lg:inline-flex']/div[@class='bet-input__field relative']/div[@class='bet-input__pin']/div/div[@class='input-form mx-auto']/div[@class='relative']/button[@class='absolute pin-r pin-t px-2 mt-03 mr-03 button-primary button-primary--gold']")
        #confirm.click() # Browser clique sur 'Confirm'
        # Annonce des règles