from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://web.whatsapp.com/')
driver.maximize_window()

contact_name = 'Rareș'
group_name = 'Te rwp rarese'
number_of_groups = 50

input('Enter anything after scanning QR')
delay = 0.6
coef = 5

for i in range(number_of_groups):
    #access the menu
    driver.find_element_by_xpath('//div[@title = "Meniu"]').click()
    time.sleep(delay)
    #click the 'New Group' option
    driver.find_element_by_xpath('//div[@aria-label = "Grup nou"]').click()
    time.sleep(delay)
    #type the name of person from your contacts which you want to spam
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div[1]/div/div/input').send_keys(contact_name)
    time.sleep(delay)
    #click on that contact
    driver.find_element_by_xpath('//span[@title = "{}"]'.format(contact_name)).click()
    time.sleep(delay)
    #click on the next step button
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/span/div/span').click()
    time.sleep(delay)
    #type the name of the group
    driver.find_element_by_xpath('//html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div/div[2]').send_keys(group_name)
    time.sleep(delay)
    #click on the last button required for creating the group
    driver.find_element_by_xpath('//html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/span/div/div').click()
    time.sleep(delay*coef)
    #after the group has been generated, we select it
    driver.find_element_by_xpath('//span[@title = "{}"]'.format(group_name)).click()
    time.sleep(delay)
    #click on group options
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[3]/div/div[2]/div/div').click()   
    time.sleep(delay*coef*0.5)
    #click on 'leave group' button
    driver.find_element_by_xpath('/html/body/div/div[1]/span[4]/div/ul/div/div/li[5]').click()
    time.sleep(delay)
    #click on accept
    driver.find_element_by_xpath('//html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]').click()
    time.sleep(delay)
    #select the group again
    driver.find_element_by_xpath('//span[@title = "{}"]'.format(group_name)).click()
    time.sleep(delay)
    #click on options
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[3]/div/div[2]/div/div').click()   
    time.sleep(delay)
    #click on 'delete group' button
    driver.find_element_by_xpath('//html/body/div/div[1]/span[4]/div/ul/div/div/li[4]/div[1]').click()   
    time.sleep(delay)
    #click on accept
    driver.find_element_by_xpath('//html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]').click()   
    time.sleep(delay)