import time
from selenium.webdriver.common.keys import Keys
from itsdangerous import exc
import csv
import os

def botStart(driver):
    driver.get('https://power.larc.nasa.gov/data-access-viewer/')
    while True:

        try:
            driver.find_element_by_xpath(
                '//*[@id="mysplash"]/div[2]/div[2]').click()
            # print('pop up removed')
            break
        except:
            # print('pop up not removed')
            pass
    print('Bot started')


def nasaDoanload(latitude, longitude,  startDate, endDate, driver):
    driver.get('https://power.larc.nasa.gov/data-access-viewer/')
    while True:

        try:
            driver.find_element_by_xpath(
                '//*[@id="mysplash"]/div[2]/div[2]').click()
            # print('pop up removed')
            break
        except:
            # print('pop up not removed')
            pass
    print('Bot started')
    # try:
    #     driver.find_element_by_xpath('//*[@id="ordermore"]').click()
    # except:
    #     pass

    while True:
        try:
            driver.find_element_by_xpath('//*[@id="usertemporal"]').click()
            # print('Clicked temporal')

            driver.find_element_by_xpath('//*[@id="hourly"]').click()
            # print('Clicked Hourly')
            # Let the user actually see something!
            driver.find_element_by_xpath('//*[@id="latdaily"]').clear()

            driver.find_element_by_xpath(
                '//*[@id="latdaily"]').send_keys(latitude)
            # print('longitude added')

            # Let the user actually see something!
            driver.find_element_by_xpath('//*[@id="londaily"]').clear()

            driver.find_element_by_xpath(
                '//*[@id="londaily"]').send_keys(longitude)
            # print('longitude added')
            break
        except:
            continue

    while True:
        try:
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@id="userformat"]').click()
            # print('User format selected')

            driver.find_element_by_xpath('//*[@id="csvbutton"]').click()
            # print('CSV selected')
            driver.find_element_by_xpath('//*[@id="Temperatures"]/i').click()

            driver.find_element_by_xpath('//*[@id="T2M_anchor"]/i[1]').click()
            # print('Temperature selected')

            driver.find_element_by_xpath(
                '//*[@id="Humidity/Precipitation"]/i').click()

            driver.find_element_by_xpath('//*[@id="RH2M_anchor"]/i[2]').click()

            break
        except:
            driver.find_element_by_xpath('/html/body').click()

            pass
            # Let the user actually see something!

    while True:
        try:

            # print('Humidity selected')
            # Let the user actually see something!
            driver.find_element_by_xpath(
                '//*[@id="hourlydatepickerstart"]').clear()

            driver.find_element_by_xpath(
                '//*[@id="hourlydatepickerstart"]').send_keys(startDate)
            driver.find_element_by_xpath(
                '//*[@id="hourlydatepickerstart"]').send_keys(Keys.ENTER)
            driver.find_element_by_xpath('//*[@id="label1"]').click()
            # print('Start Date added')

            # Let the user actually see something!
            driver.find_element_by_xpath(
                '//*[@id="hourlydatepickerend"]').clear()

            driver.find_element_by_xpath(
                '//*[@id="hourlydatepickerend"]').send_keys(endDate)
            driver.find_element_by_xpath(
                '//*[@id="hourlydatepickerend"]').send_keys(Keys.ENTER)
            driver.find_element_by_xpath('//*[@id="label1"]').click()
            # Let the user actually see something!
            driver.find_element_by_xpath('//*[@id="userinput"]').click()

            driver.find_element_by_xpath('//*[@id="testbuttondaily"]').click()
            # print('Submit')
            break
        except:
            # print("some error trying again")
            print('restart bot')
            botStart(driver)
            nasaDoanload(latitude, longitude,  startDate, endDate, driver)

            pass

    while True:
        try:
            # Let the user actually see something!
            driver.find_element_by_xpath('//*[@id="exportCSV"]').click()
            # print("download csv")
            break
        except:
            # print("some error trying to download again")

            pass


def nasaDoanload2(latitude, longitude,  startDate, endDate, driver):
    # startDate = startDate.replace("/","")
    print("Downloading File: ",longitude, latitude, startDate, )
    driver.get(f'https://power.larc.nasa.gov/api/temporal/hourly/point?Time=LST&parameters=T2M,RH2M&community=RE&longitude={longitude}&latitude={latitude}&start={startDate}&end={startDate}&format=CSV')
    time.sleep(1)
    pass


def writetoFile(StartDate, TimeValue, longitude, latitude):
    print('Opening downloaded file')
    year = StartDate[StartDate.rfind('/')+1:].zfill(4)
    dayy = StartDate[StartDate.find('/')+1:StartDate.rfind('/')].zfill(2)
    month = StartDate[:StartDate.find('/')].zfill(2)
    hour = TimeValue[:TimeValue.find(":")].zfill(2)
    longitude = round(float(longitude),2)
    latitude = round(float(latitude),2)
    longitude=str(longitude)
    latitude=str(latitude)
    longitude_bd = longitude[:longitude.find('.')].zfill(3)
    longitude_ad = longitude[longitude.find(
        '.')+1:longitude.find('.')+3].ljust(2, '0')
    latitude_bd = latitude[:latitude.find('.')].zfill(3)
    latitude_ad = latitude[latitude.find(
        '.')+1:latitude.find('.')+3].ljust(2, '0')
    hour = TimeValue[:TimeValue.find(":")]
    minute = TimeValue[TimeValue.find(":")+1:TimeValue.rfind(":")]
    second = TimeValue[TimeValue.rfind(":")+1:]
    ReadFile = f'/home/ali/Downloads/POWER_Point_Hourly_{year+month+dayy}_{year+month+dayy}_{latitude_bd}d{latitude_ad}N_{longitude_bd}d{longitude_ad}E_LST.csv'
    print('opening file: '+ReadFile)
    year = str(int(year))
    month = str(int(month))
    dayy = str(int(dayy))
    _hour = str(int(hour))
    _minute = str(int(minute))
    _second = str(int(second))
    print(_hour, _minute, _second)
    while(1):
        try:
            with open(ReadFile) as csv_file2:
                time.sleep(1)
                csv_reader2 = csv.DictReader(csv_file2, delimiter=',')
                for row2 in csv_reader2:
                
                    with open('OutputAnother.csv', 'a') as f:
                        fieldnames2 = ['Longitude', 'Latitude','Date', 'Time', 'Temperature', 'Humidity']
                        dwc = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames2)
                        # print(row2)
                        try:
                            if(row2[None][0] == month and row2[None][1] == dayy and row2[None][2] == _hour):
                                dwc.writerow({"Longitude": longitude, "Latitude": latitude, "Date": year+"/"+month+"/"+dayy,"Time": _hour+":"+_minute+":"+_second, "Temperature": row2[None][3], "Humidity": row2[None][4]})
                                os.remove(ReadFile)
                                print('written to file')
                                return True
                        except:
                            continue
                os.remove(ReadFile) 
                break
        except:
            # print("error opening downloaded file, trying agian")
            pass
            
