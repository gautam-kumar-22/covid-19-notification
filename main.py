from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r"C:\\Users\Gautam\PycharmProjects\corona_notify\corona-virus-icon-vector-29383910.ico",
        timeout=4
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        html = getData("https://mohfw.gov.in/")
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.select('div.iblock_text')[1].select('span.icount')
        total_confirmed_cases = rows[0].get_text()
        myDataStr = ""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")
        states = ['Bihar', 'Karnataka', 'Madhya Pradesh']
        total_cases = itemList[23]
        for item in itemList[0:22]:
            dataList = item.split("\n")
            if dataList[1] in states:
                nTitle = 'Cases of Covid-19'
                nText = f"Total Confirmed Cases in India: {total_confirmed_cases}\nState {dataList[1]}\n" \
                        f"Indian: {dataList[2]}, Foreign: {dataList[3]}\n" \
                        f"Cured:{dataList[4]} & Deaths: {dataList[5]}"
                notifyMe(nTitle, nText)
                time.sleep(5)
        time.sleep(10)
