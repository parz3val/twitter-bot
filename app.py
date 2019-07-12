from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime as dt

class TwitterBot():
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()
    
    def logger(self,message):
        ts = time.time()
        st = dt.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
        file_name = "Log"+st+"_.log"
        log_file = open(file_name,"a+",errors="ignore")
        log_file.write(message)
        log_file.write("\n")

    def signin(self):
        bot = self.bot
        bot.get("https://twitter.com/")

        #wait some time for the stuff to load
        time.sleep(1)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')

        email.clear()
        password.clear()

        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)


    def hashtag_search(self,hashtag):
        bot = self.bot
        #get the webpage by searching with hastags.
        url = "https://twitter.com/search?q={}&src=typd".format(hashtag)
        bot.get(url)
        

    def like_or_follow(self,hashtag,option):
        bot = self.bot
        self.hashtag_search(hashtag)
        time.sleep(3)
        if(option == "l"):
            class_name = 'HeartAnimation'
        else:
            class_name = 'not-following'
        #now, scroll the page and get the links of tweets.
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                        for elem in tweets]

            #check the options to either follow, like or do both for the given tweet
            #go through each link and click on the heart animation button to like the tweet.    
            for link in links:
                bot.get("https://twitter.com"+link)
                try:
                    like = bot.find_element_by_class_name(class_name).click()
                    time.sleep(2)
                except Exception as ex:
                    time.sleep(30)
                    self.logger(ex)
    

    #Likes and fllows the user at the same tiem with hashtag

    def follow_like(self, hashtag):
        bot = self.bot
        self.hashtag_search(hashtag)
        time.sleep(3)
        #now, scroll the page and get the links of tweets.
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]

            #check the options to either follow, like or do both for the given tweet
            #go through each link and click on the heart animation button to like the tweet.
            for link in links:
                bot.get("https://twitter.com"+link)
                try:
                    like = bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(2)
                    follow = bot.find_element_by_class_name('not-following').click()
                    time.sleep(5)
                except Exception as ex:
                    time.sleep(30)
                    self.logger(ex)
    
    #closes browser
    def close_browser(self):
        bot = self.bot
        bot.close()
        
    #automatically close browser on program exit
    
     def __exit__(self,exc_type,exc_value,traceback):
            self.close_browser()
    
botter = TwitterBot('#','#')
botter.signin()
botter.follow_like('tags')
