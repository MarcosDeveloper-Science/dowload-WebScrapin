from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def esperar_pagina_carregar(driver, timeout=20):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("Página carregada completamente.")
    except Exception as e:
        print(f"Erro ao esperar pela página carregar: {e}")
        
def waitLoading(self):
        try:
            WebDriverWait(self.browser, 1000).until(lambda driver: self.browser.execute_script('return document.readyState') == 'complete')
        except UnexpectedAlertPresentException:
            return 404
        except Exception as e:
            print("Erro não relacionado a alerta:", str(e))
        return 0

def waitLoanding(self, element):
        
        try:
            load_is_displayed = self.browser.find_element(By.XPATH, f'{element}').is_displayed()
            
            while load_is_displayed:
                try:
                    load_is_displayed = self.browser.find_element(By.XPATH, f'{element}').is_displayed()
                    time.sleep(1)
                except NoSuchElementException:
                    time.sleep(1)
                    break
                except Exception as e:
                    time.sleep(1)
                    break
        except NoSuchElementException:
            pass
        except Exception as e:
            print(f"Erro inesperado: {e}")