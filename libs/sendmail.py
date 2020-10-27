import smtplib
from configparser import ConfigParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailSender:

    def __init__(self, title=None, content=None, revicer_addr=None):
        cfg = ConfigParser()
        cfg.read('users/mail.ini')
        self.content = MIMEMultipart()
        # Specific Sender or Default Sender
        self.sender = cfg['DEFAULT']['SenderAddress']
        self.sender_secret = cfg['DEFAULT']['SenderSecret']
        if not revicer_addr:
            self.reciver = cfg['DEFAULT']['ReciverAddress']
        else:
            self.reciver = reciver_addr
        self.content['from'] = self.sender
        self.content['to'] = self.reciver

        # Load mail title if value
        if title:
            self.content['subject'] = title
        else:
            self.content['subject'] = 'The news crawler mail'

        # Load mail content if value
        if content:
            self.content.attach(MIMEText(content))

    def set_title(self, title):
        self.title = str(title)

    def set_content(self, mail_content):
        self.content.attach(MIMEText(mail_content))

    def send_mail(self):
        with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(self.sender, self.sender_secret)
                smtp.send_message(self.content)
                print("Send Mail succeed: "+str(self.reciver))
            except Exception as e:
                print("Error message: ", e)
