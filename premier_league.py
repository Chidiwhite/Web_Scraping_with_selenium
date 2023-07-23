# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the URL of the Premier League table website
driver.get("https://www.livescore.com/en/football/england/premier-league/table/")
sleep(2)

# Close the cookie consent popup
driver.find_element(By.ID, "simpleCookieBarCloseButton").click()

# Find the element containing the Premier League table
league_table = driver.find_element(By.ID, "league-table")

# Extract data for each club in the table
clubs = league_table.find_elements(By.XPATH, "//tr[contains(@id, '__league-row')]")
league_list = []

for club in clubs:
    # Extract data for each column of the table
    club_position = club.find_element(By.XPATH, "td[contains(@id, '__league-column__position')]").text
    club_name = club.find_element(By.XPATH, "td[contains(@id, '__league-column__name')]").text
    mathch_played = club.find_element(By.XPATH, "td[contains(@id, '__league-column__played')]").text
    match_won = club.find_element(By.XPATH, "td[contains(@id, '__league-column__wins')]").text
    match_draw = club.find_element(By.XPATH, "td[contains(@id, '__league-column__draws')]").text
    match_loss = club.find_element(By.XPATH, "td[contains(@id, '__league-column__losses')]").text
    goals_for = club.find_element(By.XPATH, "td[contains(@id, '__league-column__goalsFor')]").text
    goal_against = club.find_element(By.XPATH, "td[contains(@id, '__league-column__goalsAgainst')]").text
    goal_diff = club.find_element(By.XPATH, "td[contains(@id, '__league-column__goalsDiff')]").text
    club_points = club.find_element(By.XPATH, "td[contains(@id, '__league-column__points')]").text

    # Create a dictionary with the extracted data for the club
    league = {
        "club_position": club_position,
        "club_name": club_name,
        "mathch_played": mathch_played,
        "match_won": match_won,
        "match_draw": match_draw,
        "match_loss": match_loss,
        "goals_for": goals_for,
        "goal_against": goal_against,
        "goal_diff": goal_diff,
        "club_points": club_points
    }
    
    # Add the club data to the list
    league_list.append(league)

# Create a Pandas DataFrame from the list of club data
df = pd.DataFrame(league_list)

# Print the DataFrame containing the Premier League table data
print(df)

# Save the DataFrame to a CSV file named "premier.csv" (index=False to exclude row numbers)
df.to_csv('premier.csv', index=False)

# Wait for a few seconds before closing the browser
sleep(5)
