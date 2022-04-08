from selenium import webdriver

driver = webdriver.chrome(executable_path=r"C:/INTERCAMBIO_LOCAL/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.udemy.com/join/login-popup")

driver.close()