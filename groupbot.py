from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://web.whatsapp.com/')
driver.maximize_window()

CONTACT_NAME = 'foo'
GROUP_NAME = 'bar'
NUMBER_OF_GROUPS = 50
DELAY = 0.6
DELAY_COEFICIENT = 5

input('Enter anything after scanning QR\n')

for i in range(NUMBER_OF_GROUPS):
    #access the menu
    driver.find_element_by_xpath('//div[@title = "Meniu"]').click()
    time.sleep(DELAY)
    #click the 'New Group' option
    driver.find_element_by_xpath('//div[@aria-label = "Grup nou"]').click()
    time.sleep(DELAY)
    #type the name of person from your contacts which you want to spam
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div[1]/div/div/input').send_keys(CONTACT_NAME)
    time.sleep(DELAY)
    #click on that contact
    driver.find_element_by_xpath('//span[@title = "{}"]'.format(CONTACT_NAME)).click()
    time.sleep(DELAY)
    #click on the next step button
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/span/div/span').click()
    time.sleep(DELAY)
    #type the name of the group
    driver.find_element_by_xpath('//html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div/div[2]').send_keys(GROUP_NAME)
    time.sleep(DELAY)
    #click on the last button required for creating the group
    driver.find_element_by_xpath('//html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/span/div/div').click()
    time.sleep(DELAY*DELAY_COEFICIENT)
    #after the group has been generated, we select it
    driver.find_element_by_xpath('//span[@title = "{}"]'.format(GROUP_NAME)).click()
    time.sleep(DELAY)
    #click on group options
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[3]/div/div[2]/div/div').click()   
    time.sleep(DELAY*DELAY_COEFICIENT*0.5)
    #click on 'leave group' button
    driver.find_element_by_xpath('/html/body/div/div[1]/span[4]/div/ul/div/div/li[5]').click()
    time.sleep(DELAY)
    #click on accept
    driver.find_element_by_xpath('//html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]').click()
    time.sleep(DELAY)
    #select the group again
    driver.find_element_by_xpath('//span[@title = "{}"]'.format(GROUP_NAME)).click()
    time.sleep(DELAY)
    #click on options
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[3]/div/div[2]/div/div').click()   
    time.sleep(DELAY)
    #click on 'delete group' button
    driver.find_element_by_xpath('//html/body/div/div[1]/span[4]/div/ul/div/div/li[4]/div[1]').click()   
    time.sleep(DELAY)
    #click on accept
    driver.find_element_by_xpath('//html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]').click()   
    time.sleep(DELAY)
