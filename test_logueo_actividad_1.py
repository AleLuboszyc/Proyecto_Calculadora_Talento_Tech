from selenium import webdriver #Importamos la libreria que permite contralar el navegador con selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--start-maximized') # Opcional: ventana grande
driver = webdriver.Chrome(options=options) #Esta linea le dice al navegar que iniciar el navegador Chrome
driver.implicitly_wait(5) # Espera implícita profesional

try:
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
    driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title' ).text

    assert driver.title == 'Swag Labs'
    print('Título:', driver.title)  #Leemos el título de la pestaña debería salir "Swaq Labs"   
    print('Test OK')
    
finally:    
    time.sleep(10)
    driver.quit() #Cierre limpio: mata la sesión y la ventanas