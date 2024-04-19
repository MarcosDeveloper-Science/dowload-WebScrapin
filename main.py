from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from login import colocando_email,colocando_senha
from pdfManipulacao import manipulaPdf,manipulaZip
import selenium

def main():
    print(selenium.__version__)
    # Configuração do Selenium
    driver_path = "C:\\Users\\marco\\Desktop\\AutomaMP\\ManipulaDowload-WebScrapin\\chromedriver\\chromedriver-win64\\chromedriver.exe"
    options = webdriver.ChromeOptions()

    options.add_experimental_option('prefs', {
        "download.default_directory": "C:\\Users\\marco\\Desktop\\AutomaMP\\ManipulaCaoPDFPastas\\DowloadPdf",
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True
    })

    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    # Abrindo o site
    driver.get("https://mve.vivo.com.br/oauth?logout=true")
    driver.maximize_window()
    driver.implicitly_wait(10)

    colocando_email(driver)
    colocando_senha(driver)
    manipulaPdf()
    manipulaZip()


if __name__ == "__main__":
    main()
