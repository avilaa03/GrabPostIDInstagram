import time
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# Imports para evitar fechamento imediato do Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

from utils import Utils

# Códigos para evitar crash do Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
prefs = {
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2,
    "profile.default_content_setting_values.notifications": 2,
}
chrome_options.add_experimental_option("prefs", prefs)

navigator = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(navigator, 10)
pub_ids = []


class InstaScraping():

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def go_to_business_suite(self):
        navigator.get('https://business.facebook.com/')
        time.sleep(1)
        navigator.find_element('xpath', '/html/body/div/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div[6]/div/button').click()
        time.sleep(3)

    def login_input_text(self, username, password):
        self.go_to_business_suite()
        navigator.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
        time.sleep(1)
        navigator.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
        time.sleep(1)

    def enter_into_content(self):
        navigator.find_element('xpath', '//*[@id="facebook"]/body/div[1]/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/nav/ul/div/div[4]/div/div/div/li/div/div/a').click()
        time.sleep(8)

    def click_td_list(self):
        tabela = navigator.find_element('xpath', '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/table')
        linhas = tabela.find_elements('xpath', './/tbody/tr')
        for linha in linhas:
            colunas = linha.find_elements('xpath', './/td')
            for coluna in colunas:
                coluna.click()
                time.sleep(8)
                pub_ids.append(Utils.split_identifier_string(string_to_split=navigator.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[3]/span').text))
                time.sleep(2)
                navigator.find_element('xpath', '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
                time.sleep(4)
                break

    def click_login(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]')))
        navigator.find_element('xpath', '//*[@id="loginForm"]/div/div[3]').click()
        time.sleep(5)

    def run(self):
        self.login_input_text(self.username, self.password)
        self.click_login()
        self.go_to_business_suite()
        self.enter_into_content()
        self.click_td_list()
        

if __name__ == "__main__":
    username0 = "User"
    password0 = "Password"

    instaScrap = InstaScraping(username0, password0)
    instaScrap.run()

    print(pub_ids)