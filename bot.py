from re import S
from itsdangerous import exc
from pendulum import time
from webob import minute
import weather
from selenium import webdriver
import csv

driver = webdriver.Chrome('/home/ali/Documents/python/weatherBot/chromedriver')  # Optional argument, if not specified will search path.

while True:
    with open('27-02-2022.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            while(1):
                longitude = str(round(float(row["Longitude"]),4))
                latitude = str(round(float(row["Latitude"]),4))
                StartDate = str(row["Date"])
                StartDate = StartDate.replace("-","/")
                year = StartDate[StartDate.rfind('/')+1:].zfill(4)
                month = StartDate[StartDate.find('/')+1:StartDate.rfind('/')].zfill(2)
                dayy = StartDate[:StartDate.find('/')].zfill(2)
                
                StartDate = year+month+dayy
                print(StartDate)
                TimeValue = str(row["Time"])
                print("Running bot for: ",longitude, latitude, StartDate, TimeValue)
                weather.nasaDoanload2(latitude,longitude,StartDate,StartDate, driver)
                StartDate = month+"/"+dayy+"/"+year
                if(weather.writetoFile(StartDate, TimeValue, longitude, latitude)):
                    break
            

    print("DOne downloading")
    
    