import csv
import sys
import smtplib
from myinfo import SENDER_EMAIL, SENDER_PASSWORD

SEND_MSG = """ hi {} weblalbakb """
DONT_MSG = """ {} dsaf """



#file name
info_file = open('info.csv')
csv_reader = csv.reader(info_file, delimiter=',')
#next(csv_reader)

for row in csv_reader:

    name, email, accept, day, truck, language = row
    #for testing print(name, email, accept, day, truck, language)
    if name == "stephen":
        msg = SEND_MSG.format(name)
    else:
        msg = DONT_MSG.format(name)

    print("send E-mail to: {}".format(email))
    print("E-mail content:")
    print(msg) 


info_file.close()
