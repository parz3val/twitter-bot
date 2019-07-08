from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class TwitterBot():
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()
    
    def signin(self):
        bot = self.bot
        bot.get("https://twitter.com/")

        #wait some time for the stuff to load
        time.sleep(5)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')

        email.clear()
        password.clear()

        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
    
botter = TwitterBot('harriskunwar@gmail.com','1234')
botter.signin()
