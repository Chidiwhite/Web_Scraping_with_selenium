from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
from time import sleep
import pandas as pd

chrome_driver_path = 'chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com/")
sleep(5)

videos = driver.find_elements(By.TAG_NAME, "ytd-rich-item-renderer")

video_list = []
for video in videos:
    
    video_name = video.find_element(By.TAG_NAME, 'h3').text
    channel_name = video.find_element(By.TAG_NAME, "ytd-channel-name").text
    view = video.find_element(By.XPATH, ".//*[@id='metadata-line']/span[1]").text
    
    video_dict = {
        "video_name": video_name,
        "channel_name": channel_name,
        "view": view
    }
    video_list.append(video_dict)


df = pd.DataFrame(video_list)

df.to_csv('ytscrap.csv', index=False)

sleep(4)
