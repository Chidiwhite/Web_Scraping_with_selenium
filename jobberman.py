# Import necessary modules from Selenium and pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from time import sleep
import pandas as pd

# Set the path to the chromedriver executable
driver_path = "chromedriver.exe"

# Configure Chrome options to run headless
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-blink-features=AutomationControlleD")
chrome_options.add_argument("--disable-notifications")

# Initialize the Chrome WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Ask the user to input the type of job, industry, and location
_job_function = input("Type of job: ")
_industry = input("Type of industry: ")
_location = input("What is your location: ")

# Open the Jobberman website
driver.get("https://www.jobberman.com/")

# Wait for the cookie consent popup and click the "Accept" button
sleep(2)
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
sleep(1)

# Select the job function using the input value
job_dropdown = driver.find_element(By.XPATH, "//select[@aria-label='Select a job function']")
job_dropdown.click()
sleep(2)
job = driver.find_element(By.XPATH, f"//option[contains(@value, '{_job_function}')]")
job.click()
sleep(2)

# Select the industry using the input value
industry_dropdown = driver.find_element(By.XPATH, "//select[@aria-label='Select an industry']")
industry_dropdown.click()
sleep(1)
industry = driver.find_element(By.XPATH, f"//option[contains(@value, '{_industry}')]")
industry.click()

# Select the location using the input value
location_dropdown = driver.find_element(By.XPATH, "//select[@aria-label='Select a location']")
location_dropdown.click()
sleep(1)
location = driver.find_element(By.XPATH, f"//option[contains(@value, '{_location}')]")
location.click()
sleep(1)

# Click the "Submit" button to apply the selected filters
_button = driver.find_element(By.XPATH, "//button[@type='submit']")
_button.click()
sleep(3)

# Check if any jobs are found or not
no_jobs_found = driver.find_element(By.XPATH, "//span[@class='pr-2 text-gray-500']")
print(no_jobs_found.text)
sleep(3)

# Initialize a list to store job details
job_list = []

# Get a list of all job listings on the page
listed_jobs = driver.find_elements(By.XPATH, "//div[@data-cy='listing-cards-components']")

# Loop through each job listing and extract job details
for listed_job in listed_jobs:
    spans = listed_job.find_elements(By.TAG_NAME, "span")
    job_position = listed_job.find_element(By.XPATH, ".//p[@class='text-lg font-medium break-words text-link-500']").text
    company = listed_job.find_element(By.XPATH, ".//p[@class='text-sm text-link-500']").text
    location = listed_job.find_element(By.XPATH, ".//span[@class='mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide'][1]").text
    work_time = listed_job.find_element(By.XPATH, ".//span[@class='mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide'][2]").text
    salary = listed_job.find_element(By.XPATH, ".//span[@class='mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide'][3]").text
    job_function = listed_job.find_element(By.XPATH, ".//p[@class='text-sm text-gray-500 text-loading-animate inline-block']").text
    time_posted = listed_job.find_element(By.XPATH, ".//p[@class='ml-auto text-sm font-normal text-gray-700 text-loading-animate']").text
    job_description = listed_job.find_element(By.XPATH, ".//p[@class='text-sm font-normal text-gray-700 md:text-gray-500 md:pl-5']").text

    # Create a dictionary to store the job details
    _jobs_ = {
        "job_position": job_position,
        "company": company,
        "location": location,
        "work_time": work_time,
        "salary": salary,
        "job_function": job_function,
        "time_posted": time_posted,
        "job_description": job_description
    }
    
    # Append the job details dictionary to the job list
    job_list.append(_jobs_)

# Convert the list of job details into a DataFrame using pandas
df = pd.DataFrame(job_list)

# Save the DataFrame as a CSV file named "jobberman.csv" without the index column
df.to_csv("jobberman.csv", index=False)

# Wait for 3 seconds before closing the browser
sleep(3)
