# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd

# Path to the Chrome WebDriver
driver_path = "chromedriver.exe"

# Configure Chrome options to maximize the window and disable certain features
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-blink-features=AutomationControlleD")
chrome_options.add_argument("--disable-notifications")

# Create a service and initialize the WebDriver with the specified options
services = Service(driver_path)
driver = webdriver.Chrome(options=chrome_options, service=services)

# Open the URL of the website
driver.get('https://rhbooks.com.ng/')
sleep(2)

# Find all book boxes on the webpage
boxes = driver.find_elements(By.XPATH, "//div[@class='box-text box-text-products']")

# Initialize an empty list to store book details
booklist = []
for box in boxes:
    # Extract book name and price from each book box
    name = box.find_element(By.XPATH, './/p[@class="name product-title woocommerce-loop-product__title"]').text
    price = box.find_element(By.XPATH, "div[@class='price-wrapper']").text

    # Create a dictionary with book name and price
    books = {
        "Book Name": name,
        "Book Price": price
    }

    # Add the book details to the list
    booklist.append(books)

# Create a Pandas DataFrame from the list of book details
df = pd.DataFrame(booklist)

# Print the DataFrame containing book details and save it to a CSV file named "books.csv" (index=False to exclude row numbers)
print(df.to_csv('books.csv', index=False))

# Wait for a few seconds before closing the browser
sleep(3)
