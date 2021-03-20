# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 21:51:42 2021

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
browser.minimize_window()


print("Esse executável foi feito para baixar artigos direto do Sci-Hub")

print("--" * 50)

print("Tudo Pronto? \nCaso algum erro apareça abaixo, basta ignorar. \n")

print("--" * 50)

while True:
    try:
        e0 = input("Vamos começar! \nPara continuar: 'y' ou 'Y' \nPara sair: 'n' ou 'N': \n")
        if e0 in ("y", "Y"):
            e1 = int(input("Quer baixar por: \n(1) DOI \n(2) Link \n(3) Nome do Artigo \n"))
            if e1 == 1:
                doi = input("Por favor, cole o DOI: \n")
                browser.get('https://sci-hub.se/')
                print("Downloading file from: {}".format(doi))

                WebDriverWait(browser, 120)

                doi_sci = browser.find_element_by_xpath("/html/body/div[1]/div[4]/form/input[2]")
                doi_sci.send_keys(doi)
                doi_sci.send_keys(Keys.ENTER)

                WebDriverWait(browser, 120)

                openElem = browser.find_element_by_css_selector("iframe")
                browser.get(openElem.get_attribute('src'))
                    
                print("Status: Download Complete.")
                print("Folder: {}".format(dnd))
                print("--" * 50)


                e001 = input("Quer Baixar outro? y/n \n")
                if e001 in ("n", "N"):
                    print("Até a Próxima!")
                    browser.close()
                    break
                else:
                    continue
            

            elif e1 == 2:
                link = input("Por favor, coloque aqui o link para o documento: \n ")
                browser.get('https://sci-hub.se/')
                print("Downloading file from: {}".format(link))
                
                WebDriverWait(browser, 120)

                link_sci = browser.find_element_by_xpath("/html/body/div[1]/div[4]/form/input[2]")
                link_sci.send_keys(link)
                link_sci.send_keys(Keys.ENTER)
                
                WebDriverWait(browser, 120)

                openElem = browser.find_element_by_css_selector("iframe")
                browser.get(openElem.get_attribute('src'))
                
                print("Status: Download Complete.")
                print("Folder: {}".format(dnd))
                print("--" * 50)


                e001 = input("Quer Baixar outro? y/n \n")
                if e001 in ("n", "N"):
                    print("Até a Próxima!")
                    browser.close()
                    break
                else:
                    continue

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
                
                WebDriverWait(browser, 120)


                chat = browser.find_element_by_xpath("/html/body/div[1]/div[4]/form/input[2]")
                chat.send_keys(site[n-1])
                chat.send_keys(Keys.ENTER)

                WebDriverWait(browser, 120)

                openElem = browser.find_element_by_css_selector("iframe")
                browser.get(openElem.get_attribute('src'))
                
                print("Status: Download Complete.")
                print("Folder: {}".format(dnd))
                print("--" * 50)

                e001 = input("Quer Baixar outro? y/n \n")
                if e001 in ("n", "N"):
                    print("Até a Próxima!")
                    browser.close()
                    break
                else:
                    continue
 

            else:
                print("Não entendi, por favor, tente novamente!")
                 
                       
            
        elif e0 in ("n", "N"):
            print("Até a próxima! ") 
            browser.close()
            break
        
        else:
            print("--" * 50)
            print("Não Entendi.")
            print("--" * 50)
            continue



    except:
        print("Erro #01! Favor entrar em contato com o Admin (rs)")
