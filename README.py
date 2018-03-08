import csv
import sys
import smtplib
from myinfo import SENDER_EMAIL, SENDER_PASSWORD

SEND_MSG = """ hi {} weblalbakb """
DONT_MSG = """ {} dsaf """



#file name
info_file = open('info.csv')
csv_reader = csv.reader(info_file, delimiter=',')
#for some reason doesn't work makes things fail.
#next(csv_reader)

smtp = smtplib.SMTP('smtp.gmail.com')

smtp.login(SENDER_EMAIL, SENDER_PASSWORD)

for row in csv_reader:

    name, email, accept, day, truck, language = row
    #for testing print(name, email, accept, day, truck, language)
    if name == "stephen":
        msg = SEND_MSG.format(name)
    else:
        msg = DONT_MSG.format(name)
    
    smtp.sendmail(SENDER_EMAIL, email, msg)
    
smpt.close()


info_file.close()
