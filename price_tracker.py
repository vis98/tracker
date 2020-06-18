import requests
from bs4 import BeautifulSoup
import smtplib
sender_emailid=""
receiver_emailid=""
page_url="https://www.amazon.in/Redmi-Note-Pro-Electric-Processor/dp/B07X2KLYSF/ref=sr_1_2?dchild=1&keywords=mi+phone&qid=1592447492&s=electronics&sr=1-2"
browser_agent={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
def check_price():
    product_page=requests.get(page_url,headers=browser_agent)
    print(product_page)
    soup=BeautifulSoup(product_page.content,'html.parser')

    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()[2:8]
    print(title)
    print(price)
    price=price.replace(',','')
    price=float(price)
    print(price)
    if(price<16000):
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    password=""
    server.login(sender_emailid,password)

    subject='price fell'
    body='https://www.amazon.in/Redmi-Note-Pro-Electric-Processor/dp/B07X2KLYSF/ref=sr_1_2?dchild=1&keywords=mi+phone&qid=1592447492&s=electronics&sr=1-2'

    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(sender_emailid,receiver_emailid,msg)
    print('hey ur email is sent')
    server.quit()

check_price()    