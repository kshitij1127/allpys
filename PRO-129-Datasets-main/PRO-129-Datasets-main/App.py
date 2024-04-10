from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd 
from bs4 import BeautifulSoup
import time
import csv
import requests
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

service = Service(executable_path=r"C:\Users\gudla\Desktop\python\c-127\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)
browser.get(START_URL)
time.sleep(10)

headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink"]
planet_data = []
new_planets_data = []

def scrape():
    for i in range(10):
        soup = BeautifulSoup(browser.page_source, "html.parser")

        currentpage_number = int(soup.find_all("input", attrs={"class", "page_num"})[0].get("value"))
        if currentpage_number < i:
            browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        # //*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a
        elif currentpage_number > i:
            browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
        else:
            break

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
            
            hyperlink_litag = litags[0]
            temp_list.append("https://exoplanets.nasa.gov" + hyperlink_litag.find_all("a", href=True)[0]["href"])
            planet_data.append(temp_list)
            browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

scrape()
def scrape_more_data(hyperlink):
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")
        templist = []
        for trtag in soup.find_all("tr", attrs={"class":"fact_row"}):
            tdtags = trtag.find_all("td") 
            for tdtag in tdtags:
                try:
                    templist.append(tdtag.find_all("div", attrs={"class":"value"})[0].contents[0])
                except:
                    templist.append("")
        new_planets_data.append(templist)
        
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

for index, data in enumerate(planet_data):
    scrape_more_data(data[5])
    print(f"scraping at {index+1} is complete")
    
print(new_planets_data[0:1])

finalplanet_data = []
for index, data in enumerate(planet_data):
    new_planets_data_element = new_planets_data[index]
    new_planets_data_element = [elem.replace("\n", "") for elem in new_planets_data_element]
    new_planets_data_element = new_planets_data_element[:7]
    finalplanet_data.append(data + new_planets_data_element)

with open("final1.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(finalplanet_data)