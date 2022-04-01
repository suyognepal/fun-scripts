from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.firefox.options import Options

def motivation():
    browser = webdriver.Firefox(executable_path=r'D:\excersise.py\geckodriver.exe')
    motivationalvids = "https://www.youtube.com/watch?v=Z63w5PefxTQ&ab_channel=AlexKaltsMotivation" 
    browser = webdriver.Firefox()
    #browser.implicitly_wait(100)
    browser.get(motivationalvids)
    browser.find_element_by_xpath('//*[@id="movie_player"]').click()
    return
motivation()
