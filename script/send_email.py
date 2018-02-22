import smtplib
import psycopg2
import time


server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server_ssl.ehlo()

while 1:
    try:
        db = psycopg2.connect("dbname='LOG_SMS' user='postgres' host='10.10.1.38' password='postgres' port='49162'")
        cursor = db.cursor()
        break
    except:
        print "I am unable to connect to the database"
        time.sleep(60)


#Next, log in to the server
server_ssl.login("support@dialy.net", "dialy123")

#Send the mail
msg = "Hello!" # The /n separates the message from the headers
server_ssl.sendmail("support@dialy.net", "elmehdi@dialy.net", msg)
