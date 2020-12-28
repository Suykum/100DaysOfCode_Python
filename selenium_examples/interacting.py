from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "D:/udemy/chromedriver.exe"

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element_by_css_selector("#articlecount a")
#
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
fname_input = driver.find_element_by_name("fName")
fname_input.send_keys("Anna")
lname_input = driver.find_element_by_name("lName")
lname_input.send_keys("Monn")
email_input = driver.find_element_by_name("email")
email_input.send_keys("annamonn@gmail.com")
submit_button = driver.find_element_by_css_selector("form button")
submit_button.click()



driver.quit()