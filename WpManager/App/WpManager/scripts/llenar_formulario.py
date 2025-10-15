from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Selenium:
    def __init__(self, titulo, usuario, correo):
        self.titulo = titulo
        self.usuario = usuario
        self.correo = correo
        self.selenium_driver()
        self.driver.get((f"http://{self.titulo}/wp-admin/install.php"))

    def selenium_driver(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Remote(command_executor="http://selenium:4444/wd/hub", options=options)
    
    def seleccionar_idioma(self) -> None:
        idioma_es_MX = self.driver.find_element(By.CSS_SELECTOR, 'option[value=es_MX]')
        idioma_es_MX.click()
        boton_continuar = self.driver.find_element(By.ID, 'language-continue')
        boton_continuar.click()
        
    def llenar_formulario(self) -> None:
        insertar_titulo = self.driver.find_element(By.ID, 'weblog_title')
        insertar_titulo.send_keys(self.titulo)
        insertar_usuario = self.driver.find_element(By.ID, 'user_login')
        insertar_usuario.send_keys(self.usuario)
        insertar_correo = self.driver.find_element(By.ID, 'admin_email')
        insertar_correo.send_keys(self.correo)
        contrasena = self.obtener_contrasena()
        boton_instalar = self.driver.find_element(By.ID, 'submit')
        boton_instalar.click()

    def obtener_contrasena(self) -> str:
        copiar_contrasena = self.driver.find_element(By.ID, 'pass1')
        contrasena = copiar_contrasena.get_attribute("value")
        print(contrasena)
        return contrasena
    
    def desconectar_driver(self) -> None:
        self.driver.quit()

    def instalacion_wordpress(self) -> None:
        self.seleccionar_idioma()
        self.llenar_formulario()
        self.desconectar_driver()


    

nueva_instalacion = Selenium("Medicina", "Carlos Medico", "Medicina@uaz.edu.mx")
nueva_instalacion.instalacion_wordpress()