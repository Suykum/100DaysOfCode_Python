from selenium import webdriver
import time
chrome_driver_path = "C:/development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)
# bug_search = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_search.text)
# # driver.close()

event_dates = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events_data = {}
for n in range(0, len(event_names) - 1):
    events_data[n] = {
        "time": event_dates[n].text,
        "names": event_names[n].text
    }
print(events_data)
driver.quit()