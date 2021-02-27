import smtplib

# Multipurpose Internet Mail Extensions
# (Extends format of email to support sending file, audio, video and an application to the email body)
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from useridpass import username, password


def sendmail(text= None, subject='Warm Greetings', from_email='Harshal Songra <harshalsongra08@gmail.com>',
              to_emails=None):

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    msg_str = msg.as_string()

    # Login to the smtp server
    try:
        mailServer = smtplib.SMTP(host='smtp.gmail.com', port=587)
        mailServer.starttls()
        mailServer.ehlo()

        mailServer.login(username, password)

        mailServer.sendmail(from_email, to_emails, msg_str)
        mailServer.quit()

    # print Exception if occured
    except Exception as e:
        print(e)
    # We can do the same task  by With Method also like below
    # with smtplib.smtp() as mailServer:
    #     pass



