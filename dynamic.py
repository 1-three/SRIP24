# If you don't have Selenium installed, uncomment and run this line
# !pip install selenium

# Import Selenium and related modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Set up ChromeDriver for Selenium
chrome_driver_path = 'path/to/chromedriver'  # Update with the correct path to your ChromeDriver
chrome_service = Service(chrome_driver_path)

# Use headless mode for faster scraping without opening a browser window
chrome_options = Options()
chrome_options.add_argument("--headless")

# Initialize Selenium WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the dynamic website
dynamic_url = "https://in.1947partitionarchive.org/"  # Update with the actual URL
driver.get(dynamic_url)

# Wait for a specific dynamic element to ensure content is loaded
# You might need to adjust the selector depending on the site's structure
wait_time = 10  # Adjust wait time as needed
element_locator = (By.CSS_SELECTOR, 'CSS_SELECTOR_HERE')  # Adjust the CSS selector to the dynamic element
WebDriverWait(driver, wait_time).until(
    EC.presence_of_element_located(element_locator)
)

# Get the page source after the dynamic content has loaded
page_source = driver.page_source

# Parse the loaded content with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Extract specific data based on your requirements
# Example: Extract all text content
webpage_text = soup.get_text()

# Save the extracted data to a file
output_file_path = 'D:/college/starting/SRIP24/trial.txt'  # Modify the path if necessary
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(webpage_text)

print("Text has been written to:", output_file_path)

# Clean up and close the Selenium driver
driver.quit()
