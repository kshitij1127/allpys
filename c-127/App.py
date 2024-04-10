from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd 
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

service = Service(executable_path=r"C:\Users\gudla\Desktop\python\c-127\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)
browser.get(START_URL)
time.sleep(10)

headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
planet_data = []

def scrape():
    for i in range(10):
        soup = BeautifulSoup(browser.page_source, "html.parser")

        for x in soup.find_all("ul", attrs={"class", "exoplanet"}):
            litags = x.find_all("li")
            temp_list = []
            for index, litag in enumerate(litags):
                if index == 0:
                    temp_list.append(litag.find_all("a")[0].contents[0])

                else:
                    try:
                        temp_list.append(litag.contents[0])
                    except:
                        temp_list.append("")
            
            planet_data.append(temp_list)

        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()


scrape()
df = pd.DataFrame(planet_data, columns=headers)
df.to_csv("scraped_data.csv", index=True, index_label='id')