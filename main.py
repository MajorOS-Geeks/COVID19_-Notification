from plyer import notification
from bs4 import BeautifulSoup
import time
import requests 

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "icon.ico",
        timeout = 10
    )

def getData(url):
    req = requests.get(url)
    return req.text
    
if __name__ == "__main__":
    while True:
        mHtmlData = getData('https://www.mohfw.gov.in/')

        myDataStr = ""
        soup = BeautifulSoup(mHtmlData, 'html.parser')
        for tr in soup.find_all('tbody')[9].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split('\n\n')
        
        states = ['Delhi', 'Maharashtra', 'Punjab']
        for item in itemList[:23]:
            dataList = item.split('\n')
            if(dataList[1] in states):
                title = 'Cases of COVID-19'
                text = f'State : {dataList[1]}\nIndian : {dataList[2]}  Foregin : {dataList[3]}\nCured : {dataList[4]}  Death : {dataList[5]}'
                print(title)     
                
                notifyMe(title, text)

                time.sleep(3)
        time.sleep(3600)