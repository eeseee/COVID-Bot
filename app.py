from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randrange
import accountinfo

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.tweetMessages = ["Stay at home people, it's not that hard!", "Come on, we can do better Vancouver...",
         "If you can't stay at home, at least wear a mask", "We should still be social distancing Vancouver!"]
    
    def login(self):
        bot = self.bot
        bot.get("https://www.twitter.com/login")
        email = bot.find_element_by_name("session[username_or_email]")
        email.send_keys(self.username)
        password = bot.find_element_by_name("session[password]")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

    def findTweet(self):
        bot = self.bot
        bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        tweets = bot.find_elements_by_xpath("//div[@lang='en']")
        
        for tweet in tweets:
            contents = tweet.text
            if "update:" in contents:
                covidUpdate = tweet
                cases = contents[17:20]
                print(cases)
                break
        covidUpdate.click()
        return bot.current_url
    
    def retweetUpdate(self, link):
        bot = self.bot
        retweetMenu = bot.find_element_by_xpath("//div[@lang='en']//parent::div//following::div[4]")
        retweetMenu.find_element_by_xpath("//div[@data-testid='retweet']").click()
        time.sleep(3)
        bot.find_element_by_xpath("//a[@href='/compose/tweet']").click()
        time.sleep(2)
        comment = bot.find_element_by_xpath("//div[@role='textbox']")
        comment.send_keys(self.tweetMessages[randrange(4)])
        retweetButton = bot.find_element_by_xpath("//div[@data-testid='tweetButton']")
        retweetButton.click()
        


CovidBot = TwitterBot(accountinfo.username, accountinfo.password)
CovidBot.login()
tweet_link = CovidBot.findTweet()
CovidBot.retweetUpdate(tweet_link)



