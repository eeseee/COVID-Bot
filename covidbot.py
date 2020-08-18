from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.twitter.com/login")

loginInput = driver.find_element_by_name("session[username_or_email]")
loginInput.send_keys("nineteenc82@gmail.com")
passwordInput = driver.find_element_by_name("session[password]")
passwordInput.send_keys("FUCKCovid19")
loginButton = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div')
loginButton.click()
try:
    tweets = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@lang='en']"))
    )
    for tweet in tweets:
        contents = tweet.text
        if "update:" in contents:
            cases = contents[17:20]
            print(cases)
finally:
    print("success")