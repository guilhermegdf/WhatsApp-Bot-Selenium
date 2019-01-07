from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def WhathappRobot(driver):
    message_recived = {
        'primeiro':['oi','oii', 'olá', 'bom dia','boa tarde' ,'boa noite', 'hey', 'yo','hi'],
        'segundo':['1','2','3','4','5'],
        'terceiro':['obg', 'obrigado', 'tchau', 'vlw'],
    }

    message_send = {
        'segundo':{
        '1':'Envio informações.',
        '2':'Favor entre em contato com nossos atendentes ou acesse nosso site e realize seu cadastro.',
        '3':'Favor enviar número de protocolo para cancelamente.',
        '4':'Informe os dados que deseja alterar.',
        '5': 'Os testes estão sendo realizados \n Envie *Obrigado* para mensagem final.'
        },
     }

    #Busca nova mensagem recebida
    try:
        element = WebDriverWait(driver, 525600).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div._2EXPL.CxUIE"))
        )
    finally:
        element.click()
        #Pega todos os elementos dentro da div.class
        text_area = driver.find_element_by_xpath("//footer/div[1]/div[2]").get_attribute("class")
        
        #Seleciona a ultima div da lista de mensagens
        message = driver.find_elements_by_css_selector('div._9tCEa > div')
        tst_msg = driver.find_element_by_xpath("//div[@class='_9tCEa']/div["+str(len(message))+"]")
        contextGet = tst_msg.get_attribute("textContent")
        context = contextGet[:-7]

        #Pega o text da mensagem e retira os ultimos 5 campos da string pois são as horas
        print(context.lower())
        msg_box = driver.find_element_by_class_name(text_area)
        options = ['1 - Informações.', '2 - Cadastro.', '3 - Cancelamento.', '4 - Atualizar Dados.', '5 - Teste sendo realizado.\n']
        if context.lower() in message_recived['primeiro']:
            msg_box.send_keys('Bem vindo!!'+Keys.SHIFT+Keys.ENTER)
            msg_box.send_keys('Escolha uma das opções abaixo.\n')
            time.sleep(1)
            cont = 1
            for i in options:
                time.sleep(1)
                msg_box.send_keys(i+Keys.SHIFT+Keys.ENTER)

                if cont == len(options):
                    msg_box.send_keys(Keys.ENTER)
                cont =+ 1

            time.sleep(1)
            WhathappRobot(driver)
        
        if context.lower() in message_recived['segundo']:
            msg_box.send_keys(message_send['segundo'][context]+Keys.ENTER)
            time.sleep(1)
            WhathappRobot(driver)
        
        if context.lower() in message_recived['terceiro']:
            msg_box.send_keys('Volte Sempre!\n')
            time.sleep(1)
            WhathappRobot(driver)

        else:
            time.sleep(1)
            WhathappRobot(driver)

startdriver = webdriver.Chrome()
startdriver.get('http://web.whatsapp.com')
#Scan the code before proceeding further
input('Enter anything after scanning QR code')
WhathappRobot(startdriver)