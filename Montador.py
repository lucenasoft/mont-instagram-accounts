import os
import autoit
from random import choice
from random import randint
from time import sleep
from os import listdir
from os.path import isfile, join
from subprocess import SW_HIDE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


######################################### Contas no TXT #########################################
usernames = open('userdate\\date\\contas.txt','r')
lst = []
linhas = usernames.readlines()
for linha in linhas:
        lst.append(linha)
###########################################################################################################################

######################################### Inputs/Alternativas e contadores #########################################
postagens = int(input('Quantas fotos postar? '))
sexo = str(input('Qual gênero: M/F ')).upper().strip()
lst_contas = len(lst)
prontas = 0
cont_postagens = 0
###########################################################################################################################

######################################### Gerenciamento de Fotos/Pastas. #########################################
locale = os. getcwd()
path_fotos = f'{locale}\\userdate\\fotos\\'
files = [f for f in listdir(path_fotos) if isfile(join(path_fotos, f))]
cont_fotos = len(files)
a = randint(1,cont_fotos)
###########################################################################################################################

#Execução do Navegador. --> está na função #main()

###########################################################################################################################

def main():
    #######################
    global lista_user
    global lst
    global sexo
    global prontas
    global lst_contas
    global cont_fotos
    global pasta_fotos
    #######################
    while prontas < lst_contas:
        pasta_fotos = f'{locale}\\userdate\\fotos\\{files[a]}'
        global driver
        for x in range(len(lst)):
            try:
                lst_user = []
                with open('userdate\\date\\useragents.txt','r') as f:
                        while f.readline().__len__()>0:
                                lst_user.append(f.readline().strip('\n'))
                lista_user = choice(lst_user)
                print(lst[x])
                path = 'userdate\\driver' #Localização
                mobile_emulation = {
                    "deviceMetrics": { "width": 400, "height": 708, "pixelRatio": 3.0 },
                    "userAgent": f"{lista_user}"
                }
                opts = Options() #Aplicação de Opções
                opts.add_argument('--disable-blink-features=AutomationControlled') #Desativação de Automacão.
                opts.add_experimental_option("mobileEmulation", mobile_emulation)
                manager = ChromeDriverManager(path=path)
                driver = webdriver.Chrome(service=Service(manager.install()),chrome_options=opts)
                driver.set_window_size(375, 900)
                driver.get('https://www.instagram.com/')
                sleep(2)
                driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[3]/button[1]').click()
                sleep(2)
                login = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/div/label/input')
                login.click()
                login.send_keys(lst[x])
                sleep(1)
                senha = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[4]/div/label/input')
                senha.click()
                senha.send_keys('04042002')
                sleep(1)
                driver.find_element_by_xpath('//button[contains(.,"Entrar")]').click()
                sleep(5)
                cancel()
                agora_nao()
                cancel()
                notificacao()
                sleep(1)
                #biografia_gen()
                #post_perfil()
                post_feed()
                #post_story()
                logout()
                sleep(5)
                prontas += 1
            except:
                print('Não foi possível logar')
                driver.quit()
          
def agora_nao():
    try:
       sleep(2)
       driver.find_element_by_xpath('//button[contains(.,"Agora não")]').click()
       sleep(3)
    except:
        pass
    
def cancel():
    try:
       sleep(2)
       driver.find_element_by_xpath('//button[contains(.,"Cancelar")]').click()
       sleep(4)
       driver.refresh()
    except:
        pass
    
def notificacao():
    try:
       sleep(3)
       driver.find_element_by_xpath('//button[contains(.,"Agora não")]').click()
       sleep(2)
    except:
        pass

def biografia_gen():
    try:
        sleep(3)
        driver.get('https://www.instagram.com/accounts/edit/')
        biografia = driver.find_element_by_xpath('//*[@id="pepBio"]')
        biografia.click()
        sleep(1)
        biografia.send_keys(Keys.CONTROL+'A')
        sleep(2)
        biografia.send_keys('Meu brasil, meu brasil, como oh amo!')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[2]/h1')
        driver.execute_script('window.scrollTo(0,500)')
        genero_ = driver.find_element_by_xpath('//*[@id="pepGender"]')
        genero_.click()
        sleep(2)
        if sexo == 'M':
            driver.find_element_by_xpath('//*[@id="igCoreRadioButtongender1"]').click()
        if sexo == 'F':
            driver.find_element_by_xpath('//*[@id="igCoreRadioButtongender2"]').click()
        sleep(2)
        driver.find_element_by_xpath('//button[contains(.,"Concluir")]').click()
        sleep(2)
        driver.find_element_by_xpath('//button[contains(.,"Enviar")]').click()
    except:
        print('Não foi possível postar biografia ou selecionar gênero.')
        pass
    
def post_perfil():
    sleep(3)
    try: #PERFIL
        driver.get('https://www.instagram.com/accounts/edit/')
        sleep(1)
        #driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/button/img').click()
        sleep(2)
        imagem = driver.find_element_by_css_selector("input[type='file']")
        #autoit.win_active("Abrir") 
        sleep(2)
        imagem.send_keys(pasta_fotos)
        #autoit.control_send("Abrir","Edit1",pasta_fotos) 
        sleep(1)
        driver.find_element_by_xpath('//button[contains(.,"Salvar")]').click()
        #autoit.control_send("Abrir","Edit1","{ENTER}")
        sleep(2)
    except:
        print('Não foi possível postar foto de perfil')
        pass
    
def post_feed():
    global a
    global cont_postagens
    sleep(3)
    for imagens in range(0,postagens):
        try:
            a = randint(0,postagens)
            pasta_fotos = f'{locale}\\userdate\\fotos\\{files[a]}'
            driver.get('https://www.instagram.com/')
            sleep(2)
            notificacao()
            sleep(1)
            driver.find_element_by_xpath("//div[@role='menuitem']").click()
            sleep(1)
            autoit.win_set_state("Abrir",SW_HIDE)
            sleep(1)
            imagem = driver.find_element_by_css_selector("input[type='file']")
            sleep(1)
            imagem.send_keys(pasta_fotos)
            sleep(2)
            driver.find_element_by_xpath('//button[contains(.,"Avançar")]').click()
            sleep(2)
            driver.find_element_by_xpath('//button[contains(.,"Compartilhar")]').click()
            sleep(2)
            autoit.win_close("Abrir")
            cont_postagens += 1
        except:
            print('Não foi possível postar')
            pass

def post_story():
    #teste = driver.find_element_by_xpath().send_keys(Keys.CONTROL+Keys.SHIFT+'M')
    sleep(3)
    for imagens in range(0,postagens):
        try:
            a = randint(0,postagens)
            pasta_fotos = f'{locale}\\userdate\\fotos\\{files[a]}'
            driver.get('https://www.instagram.com/')
            sleep(2)
            notificacao()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[2]/div/div/div/div[1]/button').click()
            sleep(1)
            agora_nao()
            sleep(1)
            autoit.win_active("Abrir")
            sleep(1)
            autoit.control_send("Abrir","Edit1",pasta_fotos) 
            sleep(1)
            autoit.control_send("Abrir","Edit1","{ENTER}")
            sleep(1)
            driver.find_element_by_xpath('//button[contains(.,"Adicionar ao seu story")]').click()
            sleep(2)
        except:
            print('Não foi possivel postar')
            pass

def logout():
    try:
        driver.get('https://www.instagram.com/')
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[5]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[1]/div/header/div/div[1]').click()
        sleep(2)
        driver.execute_script('window.scrollTo(0,600)')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[1]/div/section/div[3]/div/div[6]/div/div/a/div[1]').click()
        sleep(1)
        driver.find_element_by_xpath('//button[contains(.,"Sair")]').click()
        sleep(2)
        driver.quit()
    except:
        driver.quit()
        pass
    
main() ######################################### FUNÇÃO PRINCIPAL START!
print(f'Foram postadas um total de {cont_postagens} fotos.')