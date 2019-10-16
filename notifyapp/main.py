import smtplib
import configparser
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def Email(**kwargs):
    config = configparser.ConfigParser()
    config.read(os.path.dirname(__file__)+'/config.ini')
    config = config["Email"]
    smtp_object = smtplib.SMTP(config["SMTP Host"], int(config["SMTP Port"]))
    smtp_object.starttls()
    smtp_object.login(config["from address"], config["password"])
    bodyMessage = ""
    for key,value in kwargs.items():
        key = key[0].upper() + key[1:]
        bodyMessage += "<strong>"+str(key)+":</strong> "+str(value)+"<br/>"
    bodyMessage = "<h3>New complaint reported</h3>"+bodyMessage
    emailMessage = MIMEMultipart()
    emailMessage['From'] = config["from address"]
    emailMessage['Subject'] = "New drug abuse complaint posted"
    emailMessage.attach(MIMEText(bodyMessage, 'html'))
    fin = open(os.path.dirname(__file__)+"/mailinglist", 'r')
    mail_to = fin.read().splitlines()
    for email_address in mail_to:
        emailMessage['To'] = email_address
        smtp_object.sendmail(config["from address"], email_address, emailMessage.as_string())
    smtp_object.quit()

def SMS():
    pass
