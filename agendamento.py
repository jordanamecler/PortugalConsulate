import os
import time
from datetime import datetime
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Ask user for cpf
CPF = input('Por favor, informe seu cpf (somente números):\n')
# Ask user for password
PSWD = getpass('Agora informe sua senha:\n')
# Set start page to crawl
URL = 'http://cloud488.hospedagem.w3br.com/public_html/'

class ConsuladoPortugalCrawler:
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.options.add_argument('--window-size=1920,1200')
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.get(URL)

    # Fills input boxes and tries to login
    def parse_login_page(self):
    	# An alert that says there is another session with same IP
    	# might show up
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass
        # Fill cpf input box
        self.driver.find_element_by_id('txtcpf').send_keys(CPF)
        # Automatically fill email input box by cliking on it
        self.driver.find_element_by_id('txtusuario').click()
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass
        time.sleep(2)
        # Fill password input box
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(PSWD)
        # Get captcha sentence that always asks for a sum of two integers
        sentence = self.driver.find_element_by_xpath("//table[@width='260']").text.replace('?', '')
        # Sum the two integers
        sum_result = sum([int(s) for s in sentence.split() if s.isdigit()])
        # Fill the captcha input box
        self.driver.find_element_by_id('BotBootInput').send_keys(str(sum_result))
        time.sleep(2)
        # Click on 'OK' to login
        self.driver.find_element_by_xpath("//input[@value='OK']").click()
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            return False
        except:
            return True
        

    # Checks if there are opened spots in calendar page
    def parse_calendar_page(self):
        if 'No momento não há vagas disponíveis.' in self.driver.page_source:
            print(datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + ' - sem vagas\n')
        else:
            print(datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + ' - novas vagas!\n')

    def check_opened_spots(self):
        if not self.parse_login_page():
            return False
        # Selects 'Registro Civil' page
        self.driver.find_element_by_xpath("//a[@onmouseover=\"self.status='Registro Civil';return true\"]").click()
        # Selects 'Agendamento' page
        self.driver.find_element_by_xpath("//a[@onmouseover=\"self.status='Agendamento';return true\"]").click()
        # Selects 'Calendar' page
        self.driver.find_element_by_xpath("//a[@onmouseover=\"self.status='Editar';return true\"]").click()
        time.sleep(2)
        self.parse_calendar_page()
        return True

    def exit_page(self):
        self.driver.quit()

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.quit()

# Starts execution
print('Starting crawler\n')
# Crawls website every 60 seconds
while True:
    crawler = ConsuladoPortugalCrawler()
    logged_in = crawler.check_opened_spots()
    crawler.exit_page()
    if not logged_in:
        print('Error loggin in, please check your cpf and password and try again.\n')
        break
    time.sleep(300)

