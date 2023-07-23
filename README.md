Scraping different websites with selenium.
1. Google Site Search using Selenium
This Python script utilizes Selenium to perform a Google search based on user input. It searches for a specific website within the search results and opens it if found. The script allows users to specify the keyword, website to search for, and the maximum number of search pages to explore. If the website is not found within the specified pages, the script notifies the user.

2. Code for Web Scraping Job Listings from Jobberman
This code uses Selenium to scrape job listings from Jobberman based on user input for job type, industry, and location. It initializes a headless Chrome browser with specific options and navigates to the Jobberman website. The code selects job, industry, and location filters based on user input, then scrapes job details (job position, company, location, work time, salary, job function, time posted, and job description). Finally, the scraped data is stored in a DataFrame and saved as a CSV file named "jobberman.csv".

3. Premier League Table Scraper
This Python script uses Selenium to scrape the current Premier League table from the website "https://www.livescore.com/en/football/england/premier-league/table/". The data is extracted and stored in a Pandas DataFrame, then saved to a CSV file named "premier.csv".

4. Rhbooks Website Scraper using Selenium
This Python script uses Selenium to scrape book details from the Rhbooks website and save them to a CSV file. It initializes the Chrome WebDriver with specific options to maximize the window and disable certain features. Then, it navigates to the Rhbooks website and extracts book names and prices from each book box on the page. The extracted data is stored in a Pandas DataFrame and then saved to a CSV file named "books.csv."

5. YouTube Video Scraping with Python and Selenium
This Python script demonstrates web scraping using Selenium to extract video details from the YouTube homepage. It automates a web browser, finds video elements, and extracts video name, channel name, and view count. The extracted data is stored in a Pandas DataFrame and saved as 'ytscrap.csv'. This script provides a practical example of how to gather information from web pages dynamically using Selenium and Python
