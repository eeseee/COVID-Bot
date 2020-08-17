from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.twitter.com/login")

loginBox = driver.find_element_by_name("session[username_or_email]")
loginBox.send_keys("nineteenc82@gmail.com")
passwordBox = driver.find_element_by_name("session[password]")
passwordBox.send_keys("FUCKCovid19")
loginButton = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div')
loginButton.click()