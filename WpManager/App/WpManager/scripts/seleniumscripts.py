from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import tempfile

def formFill(siteTitle, username, email, authWordpress):
    time.sleep(20)
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
# Crear instancia del navegador con el perfil temporal
    driver = webdriver.Chrome(options=options)
    driver.get(f"http://{siteTitle}")
    selectLanguage = driver.find_element(By.XPATH, "/html/body/form/select/option[39]")
    selectLanguage.click()
    continueButton = driver.find_element(By.ID, 'language-continue')
    continueButton.click()
    siteTitleBox = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[1]/td/input')
    siteTitleBox.send_keys(siteTitle)
    usernameBox = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/input')
    usernameBox.send_keys(username)
    emailBox = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[6]/td/input')
    emailBox.send_keys(email)
    passwordBox = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[3]/td/div/div/input')
    copiedPassword = passwordBox.get_attribute("value")
    print(type(copiedPassword))
    authWordpress.wpPassword = copiedPassword
    installWpsBtn = driver.find_element(By.XPATH, '/html/body/form/p/input')
    installWpsBtn.click()
    login = driver.find_element(By.XPATH, '/html/body/p[3]/a')
    login.click()
    # driver.save_screenshot('screenshot.png')
    return copiedPassword

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
# Crear instancia del navegador con el perfil temporal
driver = webdriver.Remote(
    command_executor="http://selenium:4444/wd/hub",
    options=options
)
driver.get(f"https://github.com/AkuseruGH")
# selectLanguage = driver.find_element(By.XPATH, "/html/body/form/select/option[39]")
# selectLanguage.click()
# continueButton = driver.find_element(By.ID, 'language-continue')
# continueButton.click()
driver.save_screenshot("./screenshot.png")
print("hola")
driver.quit()
# siteTitleBox = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[1]/td/input')
# siteTitleBox.send_keys(siteTitle)
# usernameBox = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/input')
# usernameBox.send_keys(username)
# emailBox = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[6]/td/input')
# emailBox.send_keys(email)
# passwordBox = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[3]/td/div/div/input')
# copiedPassword = passwordBox.get_attribute("value")
# print(type(copiedPassword))
# installWpsBtn = driver.find_element(By.XPATH, '/html/body/form/p/input')
# installWpsBtn.click()
# login = driver.find_element(By.XPATH, '/html/body/p[3]/a')
# login.click()
# # driver.save_screenshot('screenshot.png')