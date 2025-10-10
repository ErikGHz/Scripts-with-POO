from selenium import webdriver
from selenium.webdriver.common.by import By

def rellenar_formulario(titulo, usuario, correo):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
# Crear instancia del navegador con el perfil temporal
    web_driver = webdriver.Remote(
    command_executor="http://selenium:4444/wd/hub",
    options=options
    )
    web_driver.get(f"http://{titulo}")
    seleccionar_idioma = web_driver.find_element(By.XPATH, "/html/body/form/select/option[35]")
    seleccionar_idioma.click()
    boton_continuar = web_driver.find_element(By.ID, 'language-continue')
    boton_continuar.click()
    insertar_titulo = web_driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[1]/td/input')
    insertar_titulo.send_keys(titulo)
    insertar_usuario = web_driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/input')
    insertar_usuario.send_keys(usuario)
    insertar_correo = web_driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[6]/td/input')
    insertar_correo.send_keys(correo)
    get_contrasena = web_driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[3]/td/div/div/input')
    contrasena = get_contrasena.get_attribute("value")
    print(contrasena)
    boton_instalar = web_driver.find_element(By.XPATH, '/html/body/form/p/input')
    boton_instalar.click()
    login = web_driver.find_element(By.XPATH, '/html/body/p[3]/a')
    login.click()
    web_driver.quit()