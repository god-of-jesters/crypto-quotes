from bs4 import BeautifulSoup
import requests
import datetime
import sqlite3
import time
con = sqlite3.connect('cripto')
cursor = con.cursor()
# cursor.execute('CREATE TABLE cripto1(data text,curs int)')
#con.commit()
#Создание базы данных
while True:
    dt = datetime.datetime.now()
    time1 = f"{dt.hour}:{dt.minute}:{dt.second}"
    rec = requests.get('https://bcs-express.ru/kotirovki-i-grafiki/btcusd')
    soup = BeautifulSoup(rec.content, 'lxml')

    curs = soup.find('div',class_="quote-head__price-value js-quote-head-price js-price-close").text
    print(curs)
    curs = list(curs)
    curs[curs.index(',')] = '.'
    curs.pop(2)

    curs = float(''.join(curs))
    print(type(time1))
    print(curs)
    print(f'INSERT INTO crip2 Values(\"{time1}\",{curs});')
    cursor.execute(f'INSERT INTO crip2 Values(\"{time1}\",{curs});' )
    con.commit()
    time.sleep(60)
