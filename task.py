import smtplib
from email.message import EmailMessage
import datetime
import time
import schedule 

def automatic():
    day = datetime.datetime.today()
    time = datetime.datetime.now()

    my_custom = day.strftime("%B %d %Y")
    current_time = time.strftime("%I:%M:%S")


    mail="job.ahmedpiprani@gmail.com"
    password="euae feev udlr lgby"

    connect=smtplib.SMTP("smtp.gmail.com")
    connect.starttls()

    msg=EmailMessage()
    msg["FROM"]=mail
    msg["To"]="work.ahmadpiprani@gmail.com"
    msg["Cc"]="ma4928y@gmail.com"
    msg.add_header("Subject","EMERGENCY OCCUR !")
    msg.set_content("Read this file carefully.")

    with open("hello.txt","rb") as file:
        attach=file.read()
        file_name=file.name
        msg.add_attachment(attach, maintype="application", subtype="octet-stream", filename=file_name)
    

    connect.login(user=mail,password=password)
    connect.send_message(msg)
    connect.close()
    print("mail hasbeen sent")
schedule.every().tuesday.at("10:38").do(automatic)
while True:
    schedule.run_pending()
    time.sleep(1)    