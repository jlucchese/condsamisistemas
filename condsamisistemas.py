# This Python file uses the following encoding: utf-8
#
# CONDSAMISISTEMAS
# This script will log in the samisistemas customer system and check if a condominium bill existed, notifying the user by email

import requests
import smtplib
import sqlite3

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, date

# configs
d = {'usuario':'','senha':''}
email_to = ''
email_from = ''

# samisistemas variables
url = "https://clienteonline.samisistemas.com.br/"
url_login = url+'login.php'
url_bill = url+'2viaboleto.php'
p = {'sigla':'nee'}

# get cookie
print('Getting cookies from samisistemas')
r = requests.get(url_login, params=p)
c = r.cookies
u = r.url

# login
print('Logging in the samisistemas customer system')
r = requests.post(url_login, params=p, data=d, cookies=c)
c = r.cookies

# check if bill are listed and send alert
print('Checking if there is a bill listed')
r = requests.get(url_bill, data=d, cookies=c)
if 'Nao foi localizado nenhum Boleto' not in r.text:
    print('Bill was found')
    conn = sqlite3.connect('condsamisistemas.db')
    c = conn.cursor()

    # check if table 'alerts' exists, otherwise create it
    try:
        c.execute("SELECT * FROM alerts")
    except sqlite3.OperationalError:
        c.execute("CREATE TABLE alerts (send_date date)")

    # check ir alert was already sent
    t = (datetime.now().date(),)
    c.execute("SELECT * FROM alerts WHERE date(send_date,'start of month') == date(?,'start of month')", t)

    print('Checking if notification was already sent')
    if c.fetchone() is None:
        c.execute("INSERT INTO alerts VALUES (?)", t)
        conn.commit()
        conn.close()
        msg = MIMEMultipart()
        msg['Subject'] = 'Boleto de condomínio'
        msg['From'] = email_from
        msg['To'] = email_to
        text = 'Seu boleto já está disponível para download no site '+u.encode('utf-8')
        msg.attach(MIMEText(text,'plain',_charset='UTF-8'))

        print('Sending notification to customer by email')
        s = smtplib.SMTP('localhost')
        s.sendmail(email_from, email_to, msg.as_string())
    else:
        print('Notification was already sent')
else:
    print('There is no bill')
