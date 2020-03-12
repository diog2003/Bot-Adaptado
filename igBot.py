from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #self.profile = 'dollynhocoach'
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\Serjao\\Desktop\\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(10)
        '''
        botao_login = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        botao_login.click()
        ''' 
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)

        time.sleep(7)

        self.comente_no_sorteio('p/B8ujLBplVLk')
        
    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comente_no_sorteio(self,sorteio):
        driver = self.driver
        driver.get("https://www.instagram.com/"+ sorteio +"/")
        time.sleep(5) 
        
        contador=0
        while(0!=1):
            try:
                comentarios = ["@karolabreu5","@delainefinatti","@deisefm26","@gisa1915","@glyra366","@deisefinatti","@don.bre","@slssaraiva","@erikabsaraiva","@lgsaraiva76","@duduabreuly","@isa_fs","@finattiandre","@andressafinatti","@christianefinatti","@rodzin25","@guiespinati","@leodelanda","@yasmimvancelotte","@rodslvrio","@gomes_briann","@nathilial","@biazete","@lucassdamess","@yagovillar07","@g_andre98","@rafaelteixeira_s","@thales300","@mikaela_alves42","@beccamnoel","@carollsimplicio","@carol.passos","@bebelarezende","@drumond_ste","@pedroaraujorodrigues_","@vicentinho_york","@hellengabrielaa","@juamanciom","@ziul6","@diixlyra","@cnevesss"]
                i=0
                while(i!=2):
                    driver.find_element_by_class_name("Ypffh").click()
                    campo_comentario = driver.find_element_by_class_name("Ypffh")
                    time.sleep(random.randint(2,5))
                    self.digite_como_uma_pessoa(random.choice(comentarios),campo_comentario)
                    time.sleep(random.randint(3,5))
                    campo_comentario.send_keys(Keys.RETURN)
                    campo_comentario.send_keys(Keys.RETURN)
                    campo_comentario.send_keys(Keys.RETURN)
                    contador = contador + 1
                    print(contador)
                    i = i + 1
                    time.sleep(random.randint(5,9))
                time.sleep(random.randint(300,600))
            except Exception as e:
                print(e)
                time.sleep(5)

javiBot = InstagramBot('saraivamarcus18',"080117")
javiBot.login()