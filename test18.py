import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "qudgjsdl13@gmail.com" # gmail address
gmail_pwd = "gksqufdl45!" # gmail password

def send_gmail(to, subject, text, attach):
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText())
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()

def plus():
    hap=0
    i=int(input("정수를 입력해 주세요:"))

    for i in range(1,i+1,1):
       if i%3==0:
           continue

       hap +=i

    print("%d 까지의 합(3의 배수 제외):%d" %(i,hap))

send_gmail("qudgjsdl13@naver.com","파이썬 연습",plus(),)