from selenium.webdriver.common.by import By

def colocando_email(driver):
    input_email = driver.find_element(By.XPATH,'/html/body/main/div/div/div/div[2]/form/div[2]/span/div/div/input')
    input_email.send_keys('mar.p@gmail.com')

def colocando_senha(driver):
    input_senha = driver.find_element(By.XPATH,'/html/body/main/div/div/div/div[4]/form/div[2]/span/div/div/input')
    input_senha.send_keys('12345')