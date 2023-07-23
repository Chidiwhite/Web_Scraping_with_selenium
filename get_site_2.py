# Import required modules from Selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

# Set up Chrome WebDriver and options
driver_path = "C:/SeleniumWebdrivers/chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-blink-features=AutomationControlleD") 
chrome_options.add_argument("--disable-notifications")
service = Service('chromedriver.exe')

# Get user inputs
url = 'http://www.google.com/'
keyword = input('Enter word to search: ')
site_to_get = input('Enter site to get: ')
max_pages = int(input('pages to search'))

# Create WebDriver instance
driver = webdriver.Chrome()
driver.get(url)
sleep(2)

# Find the search bar element and enter the keyword
search_bar = driver.find_element(By.XPATH, "//textarea[@class = 'gLFyf' and @aria-label='Search']")
search_bar.send_keys(keyword)
sleep(3)
search_bar.send_keys(Keys.ENTER)

# Initialize variables for site search
site_not_found = True
page_number = 0

# Loop through Google search pages to find the desired site
while site_not_found:
    page_number += 1
    each_container = driver.find_elements(By.TAG_NAME, 'a')
    all_site = [container.get_attribute('href') for container in each_container]
    for site in all_site:
        # Check if the desired site is found in the search results
        if site is not None and site_to_get in site:
            print('Site found in page: ', page_number)
            sleep(2)
            driver.get(site)
            sleep(3)
            driver.quit()
            site_not_found = False
            break

    # Check if the maximum number of search pages has been reached
    if page_number == max_pages:
        print(f"Your site was not found in the first {max_pages} pages of Google search.")
        break

    # If site is not found yet, go to the next search page
    if site_not_found:
        next_button = driver.find_element(By.XPATH, '//span[@style="display:block;margin-left:53px"]')
        next_button.click()
        sleep(2)
