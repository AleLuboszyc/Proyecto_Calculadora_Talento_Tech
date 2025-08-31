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
    assert driver.title == 'Swag Labs'
    print('Título:', driver.title)  #Leemos el título de la pestaña debería salir "Swaq Labs"
    print('Test OK')
    
    seccion_productos = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title' ).text #Esta línea le dice a Selenium que busque un solo elemento en la página que coincida con el selector CSS que le diste, y lo guarda en la variable que declare.
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')   #Busca todos los elementos en la página que tengan la clase inventory_item. Cuando los encuentra, los guarda todos juntos en una lista que se llama productos y la voy a inicializar en 0.
    nombre_del_producto = productos[0].find_element(By.CLASS_NAME, 'inventory_item_name').text 
    precio_del_producto = productos[0].find_element(By.CLASS_NAME, 'inventory_item_price').text
    assert seccion_productos == 'Products' #Es una validacion de la seccion sea la correcta
    assert len(productos) > 0 #Cuenta cuantos elementos hay en la lista productos.
    print('Esta es la sección de productos:', seccion_productos)
    print('Cantidad de productos en inventario:', len(productos))
    print('El primer producto es:', nombre_del_producto, 'y su precio es:', precio_del_producto)
    
    productos[0].find_element(By.CLASS_NAME, 'btn_inventory').click() #Hace click en el boton de agregar al carrito del primer producto
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click() #Hace click en el carrito de compras
    producto_agregado_al_carrito = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text #Busca el elemento que tiene la clase shopping_cart_badge y obtiene su texto
    producto_en_el_carrito = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text #Busca el nombre del producto en el carrito
    assert producto_en_el_carrito == 'Sauce Labs Backpack' #Valida que el producto en el carrito sea el correcto
    assert producto_agregado_al_carrito == '1' #Valida que el texto del carrito sea 1
    print('Cantidad de productos agregados al carrito:', producto_agregado_al_carrito)
    print('El producto en el carrito es:', producto_en_el_carrito)
    
finally:  
    time.sleep(10) #Mantener la ventana abierta 10 segundos para que veas el resultado
    driver.quit() #Cierre limpio: mata la sesión y la ventanas