import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_to = ["user@mail.com","user2@mail.com","user3@mail.com"] #the seonnd one is the professor, the third one is me



def send(link):
    username = "user@mail.com"
    password = "password"
    mail_from = "user@mail.com"
    mail_subject = "Meeting Reminder"
    mail_body = " Hi,\n Hope you are doing great.\n" \
                " On behalf of the host, I found you are late 1 min on today's meeting, please join immediately throung the link: \n" +link

    mimemsg = MIMEMultipart()
    mimemsg['From']=mail_from
    mimemsg['To']=", ".join(mail_to)
    mimemsg['Subject']=mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))
    connection = smtplib.SMTP(host='smtp.office365.com', port=587)
    #connection = smtplib.SMTP(host='smtp.office365.com', port=25)

    connection.starttls()
    connection.login(username,password)
    connection.send_message(mimemsg)
    connection.quit()


def sendGreet(link):
    username = "user@mail.com"
    password = "password"
    mail_from = "user@mail.com"
    mail_subject = "Welcoming Email"
    mail_body = " Hi,\n Hope you are doing great.\n" \
                " On behalf of the host, I would like to invite you to join, please join immediately throung the link: \n" + link

    mimemsg = MIMEMultipart()
    mimemsg['From'] = mail_from
    mimemsg['To'] = ", ".join(mail_to)
    mimemsg['Subject'] = mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))
    connection = smtplib.SMTP(host='smtp.office365.com', port=587)
    # connection = smtplib.SMTP(host='smtp.office365.com', port=25)

    connection.starttls()
    connection.login(username, password)
    connection.send_message(mimemsg)
    connection.quit()

def sendMem(link,num):
    username = "user@mail.com"
    password = "password"
    mail_from = "mail@mail.com"
    mail_subject = "Reminder Email"
    mail_body = " Hi,\n Hope you are doing great.\n" \
                " On behalf of him, I found you are late 1 min on today's meeting, please join immediately throung the link: \n" + link

    mimemsg = MIMEMultipart()
    mimemsg['From'] = mail_from

    if num ==1:
        mimemsg['To'] = 'user1k@mail.com' # professor email
    elif num == 2:
        mimemsg['To'] = 'user2@gmail.com'  # late student email
    mimemsg['Subject'] = mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))
    connection = smtplib.SMTP(host='smtp.office365.com', port=587)
    # connection = smtplib.SMTP(host='smtp.office365.com', port=25)

    connection.starttls()
    connection.login(username, password)
    connection.send_message(mimemsg)
    connection.quit()
