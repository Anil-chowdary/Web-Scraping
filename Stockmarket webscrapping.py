from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pandas as pd
import time

driver = webdriver.Chrome()

url = "https://finviz.com/"
driver.get(url)

    # Pause to allow the page to load fully
time.sleep(3)

    # Find the stock table on the homepage
table = driver.find_element(By.ID, 'js-signals_1')

    # Get all rows from the table
rows = table.find_elements(By.TAG_NAME, 'tr')

    # Initialize a list to hold stock information
stocks_data = []

   # Loop through the rows and extract relevant data (Company name, Price, Change, Volume)
for row in rows[1:]:  # Skip the header row
        cells = row.find_elements(By.TAG_NAME, 'td')
        if len(cells) > 1:
            try:

                company = cells[0].text.strip()
                price = cells[1].text.strip()
                change = cells[2].text.strip()
                volume = cells[3].text.strip()

                stocks_data.append([company, price, change, volume])
            except IndexError:
                # If any issue occurs while scraping a row, we can skip it
                continue

    # Close the WebDriver session
driver.quit()
print(stocks_data)
import pandas as pd

df = pd.DataFrame(stocks_data)

# Save DataFrame to a CSV file
df.to_csv('stocks_data.csv', index=False)