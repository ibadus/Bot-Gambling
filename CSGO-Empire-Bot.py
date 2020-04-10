import time
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

# Fonctions
def TERRO(browser, mise):
    bet = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[5]/div/div[1]/input")
    bet.send_keys(mise) #mise la mise #PAS bmise
    cote = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[7]/div[3]/div/div/button/div/div[1]/div/span")
    cote.click()

def CT(browser, mise):
    bet = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[5]/div/div[1]/input")
    bet.send_keys(mise) #mise la mise #PAS bmise
    cote = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[7]/div[1]/div/div/button/div/div[1]/div/span")
    cote.click()

def win(mise, bmise):
    mise = bmise

def loose(mise):
    mise = mise * 2

# Inputs
bmise = str(input("Entrez la mise voulue : "))
couleur = str(input("CT ou TERRO : "))
retrait = int(input("Nombre de lose de suite maximum : "))
userpin = str(input("Entrez votre PIN : "))

# Annonce des règles
print("Vous avez choisis {} comme mise de base qui sera *2 lorsque vous perderez.\nLe bot s'arrêtera lorsque vous aurez fait {} défaites de suites.\nVous miserez uniquement sur le côté {}.".format(bmise,retrait,couleur))

# Variables
url = "https://csgoempire.com/"
mise = bmise
i = 0
timer = 0
start = 1

# Début du programme
    # Ouverture du navigateur
        # Option = ouvrir le browser sur l'utilisateur actuel
chrome_options = Options()
chrome_options.add_argument('--user-data-dir=C:\\Users\\VOTRE NOM D UTILISATEUR\\AppData\\Local\Google\\Chrome\\User Data') ##################################### A CHANGER ##################################### 
capabilities = DesiredCapabilities.CHROME.copy()
chromedriver = "C:\\Users\\VOTRE NOM D UTILISATEUR\\chromedriver.exe" ##################################### A CHANGER ##################################### 
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options = chrome_options, desired_capabilities=capabilities) # Ouverture de Chrome
browser.get(url) # Ouvre l'URL

    # Lancement du programme
browser.implicitly_wait(5) # Browser attends 5 secondes
pin = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[5]/div/div[1]/div[1]/div/div/div/input")
pin.send_keys(userpin) # Brwoser entre le PIN
confirm = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[5]/div/div[1]/div[1]/div/div/div/button")
confirm.click() # Browser clique sur 'Confirm'

print("===========================\n'A' pour LANCER le programme sur l'invite de commande.")
print("===========================\nESC pour QUITTER le programme sur l'invite de commande.\n===========================")

time.sleep(5)
balance = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/span/span").text
print("Vous avez {} dans votre balance".format(balance))
print("===========================")
keyboard.wait('a')
if couleur == "TERRO":
    while i < retrait :
        while str(timer) != "15,00":
            timer = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[4]/div[2]/div/div[2]").text
            if keyboard.read_key() == 'esc':
                print("Fermeture du programme...")
                browser.quit()
                quit()
        newbalance = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/span/span").text
        TERRO(browser, mise)
        while str(start) != "0,00":
            start = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[7]/div[2]/div/div[1]/div[2]/span").text
            if keyboard.read_key() == 'esc':
                print("Fermeture du programme...")
                browser.quit()
                quit()
        if newbalance > balance :
            win(mise, bmise)
        elif newbalance < balance :
            loose(mise)
            i = i + 1
        elif keyboard.read_key() == 'esc':
            print("Fermeture du programme...")
            browser.quit()
            quit()
        print("New game....")
        balance = newbalance

if couleur == "CT":
    while i < retrait :
        while str(timer) != "15,00":
            timer = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[4]/div[2]/div/div[2]").text
            if keyboard.read_key() == 'esc':
                print("Fermeture du programme...")
                browser.quit()
                quit()
        newbalance = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/span/span").text
        CT(browser, mise)
        while str(start) != "0,00":
            start = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/section/div/div/div[7]/div[2]/div/div[1]/div[2]/span").text
            if keyboard.read_key() == 'esc':
                print("Fermeture du programme...")
                browser.quit()
                quit()
        if newbalance > balance :
            win(mise, bmise)
        elif newbalance < balance :
            loose(mise)
            i = i + 1
        elif keyboard.read_key() == 'esc':
            print("Fermeture du programme...")
            browser.quit()
            quit()
        print("New game....")
        balance = newbalance