# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:23:17 2021

@author: Dutt
"""

from googlesearch import search 
import google
import selenium as sln
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



print("Sci-Hub Downloader V1 \n", 50 * "-")
print("\n \nEssa é uma versão teste. \n Existem alguns bugs conhecidos, para saber mais veja o Readme.txt")

print("\n \n", 50 * "-" )

# Abrindo o ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument("start-minimized")
options.add_argument("--disable-extensions")
options.add_argument("window-size=1200x600")

dnd = input("Em qual pasta você gostaria de armazenar os downloads? ")             

profile = {"plugins.always_open_pdf_externally": True,
           "download.default_directory" : dnd}

options.add_experimental_option("prefs", profile)

browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)

# Começando o executável:

print("Esse executável foi feito para baixar artigos direto do Sci-Hub")

# e0: Ready? (para tentar burlar o bug conhecido dessa versão do ChromeDriverManager)
e0 = input("Tudo Pronto? y/n \n \nCaso algum erro apareça abaixo, basta ignorar. Pronto? y/n  \n")


# 1o Loop:
while e0 in ("N", "n"):
    e0 = input("Pronto para começar? y/n \n")
if e0 in ("Y", "y"):
    e1 = int(input("Utilizaremos: \n (1) DOI \n (2) Link \n (3) Nome do Artigo \n"))
    if e1 == 1:
        doi = input("Por favor, coloque aqui o DOI para o documento: \n ")
        browser.get('https://sci-hub.se/')
        print("Downloading file from: {}".format(doi))

        doi_sci = browser.find_element_by_xpath("/html/body/div[1]/div[4]/form/input[2]")
        doi_sci.send_keys(doi)
        doi_sci.send_keys(Keys.ENTER)
        openElem = browser.find_element_by_css_selector("iframe")
        browser.get(openElem.get_attribute('src'))
        
        print("Status: Download Complete.")
        print("Folder: {}".format(dnd))
    elif e1 == 2:
        link = input("Por favor, coloque aqui o link para o documento: \n ")
        browser.get('https://sci-hub.se/')
        print("Downloading file from: {}".format(link))
        
        link_sci = browser.find_element_by_xpath("/html/body/div[1]/div[4]/form/input[2]")
        link_sci.send_keys(link)
        link_sci.send_keys(Keys.ENTER)
        openElem = browser.find_element_by_css_selector("iframe")
        browser.get(openElem.get_attribute('src'))
        
        print("Status: Download Complete.")
        print("Folder: {}".format(dnd))
    elif e1 == 3:
        nome = input("Por favor, qual o nome do artigo? \n ")
        site = list()
        for j in search(nome, tld="co.in", num=10, stop=10, pause=2): 
            site.append(j) 
        print("Os sites são: \n")
        for i in range(len(site)): 
            print (i + 1, end = " ") 
            print (site[i]) 
        n = int(input("Desses links, de qual você quer baixar? \n "))
        browser.get('https://sci-hub.se/')
        print("Downloading file: {}".format(nome))
        
        chat = browser.find_element_by_xpath("/html/body/div[1]/div[4]/form/input[2]")
        chat.send_keys(site[n-1])
        chat.send_keys(Keys.ENTER)
        openElem = browser.find_element_by_css_selector("iframe")
        browser.get(openElem.get_attribute('src'))
        
        print("Status: Download Complete.")
        print("Folder: {}".format(dnd))
 
    
inputAgain = input("Deseja baixar outro? \n ")
if inputAgain in ("n", "N"):
        print("Muito Obrigado \n ", 50 * "=")     
        browser.close() 
        
while inputAgain in ("y", "Y"):
    e0 = input("Tudo Pronto? y/n \n ")

    # 1o Loop:
    while e0 in ("N", "n"):
        e0 = input("Pronto para começar? y/n \n")
    if e0 in ("Y", "y"):
        e1 = int(input("Utilizaremos: \n (1) DOI \n (2) Link \n (3) Nome do Artigo \n"))
        if e1 == 1:
            doi = input("Por favor, coloque aqui o DOI para o documento: \n ")
            browser.get('https://sci-hub.se/')
            print("Downloading file from: {}".format(doi))
            
            doi_sci = browser.find_element_by_xpath("/html/body/div[1]/div[4]/form/input[2]")
            doi_sci.send_keys(doi)
            doi_sci.send_keys(Keys.ENTER)
            openElem = browser.find_element_by_css_selector("iframe")
            browser.get(openElem.get_attribute('src'))
            
            print("Status: Download Complete.")
            print("Folder: {}".format(dnd))
            inputAgain = input("Wanna go Again: y/n ")

        elif e1 == 2:
            link = input("Por favor, coloque aqui o link para o documento: \n ")
            browser.get('https://sci-hub.se/')
            print("Downloading file from: {}".format(link))
            
            link_sci = browser.find_element_by_xpath("/html/body/div[1]/div[4]/form/input[2]")
            link_sci.send_keys(link)
            link_sci.send_keys(Keys.ENTER)
            openElem = browser.find_element_by_css_selector("iframe")
            browser.get(openElem.get_attribute('src'))
            
            print("Status: Download Complete.")
            print("Folder: {}".format(dnd))
            inputAgain = input("Wanna go Again: y/n ")

        elif e1 == 3:
            nome = input("Por favor, qual o nome do artigo? \n ")
            site = list()
            for j in search(nome, tld="co.in", num=10, stop=10, pause=2): 
                site.append(j) 
            print("Os sites são: \n")
            for i in range(len(site)): 
                print (i + 1, end = " ") 
                print (site[i]) 
            n = int(input("Desses links, de qual você quer baixar? \n "))
            browser.get('https://sci-hub.se/')
            print("Downloading file: {}".format(nome))
            
            chat = browser.find_element_by_xpath("/html/body/div[1]/div[4]/form/input[2]")
            chat.send_keys(site[n-1])
            chat.send_keys(Keys.ENTER)
            openElem = browser.find_element_by_css_selector("iframe")
            browser.get(openElem.get_attribute('src'))
            
            print("Status: Download Complete.")
            print("Folder: {}".format(dnd))
            inputAgain = input("Wanna go Again: y/n ")

    if inputAgain in ("n", "N"):
        print("Buh-bye")     
        browser.close() 

