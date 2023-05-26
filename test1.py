
       

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


webdriver_service = Service('/path/to/chromedriver')

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode

# Initialize the ChromeDriver instance
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# File to upload
file_path = '/path/to/upload/file.txt'

# URL of the page with the upload functionality
upload_page_url = 'https://example.com/upload'

# Open the upload page
driver.get(upload_page_url)

# Locate the file input element
file_input = driver.find_element(By.ID, 'file-input')

# Send the file path to the file input element
file_input.send_keys(file_path)

# Wait for the file to be uploaded
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, 'file-upload-progress')))

# Click on the download link
download_link = driver.find_element(By.XPATH, '//a[contains(@href, "download")]')
download_link.click()


driver.quit()
