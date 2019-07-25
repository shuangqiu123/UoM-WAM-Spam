"""
SMTP-based Gmail notifier

:author: Matthew Farrugia-Roberts
"""

import getpass
import smtplib
from email.mime.text import MIMEText


GMAIL_SMTP_HOST = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587


class SMTPGmailNotifier:
    def __init__(self, address=None, password=None, smtp_host=GMAIL_SMTP_HOST,
                    smtp_port=GMAIL_SMTP_PORT):
        """
        :param address: The email address to use (as all three of SMTP login 
                        username, email sender, and email recipient).
        :param password: The password to use for SMTP server login.
        :param smtp_host: Name of the SMTP server.
        :param smtp_port: Port of the SMTP server.
        """
        print("Configuring SMTP Gmail Notifier...")
        if address is not None:
            self.address = address
        else:
            self.address = input("Email address: ")
        if password is not None:
            self.password = password
        else:
            self.password = getpass.getpass()
        self.host = smtp_host
        self.port = smtp_port

    def notify(self, subject: str, text: str) -> None:
        """
        Send a self-email.

        :param subject: The email subject line.
        :param text: The email body text.
        """
        print("Sending an email to self...")
        print("From/To:", self.address)
        print("Subject:", subject)
        print("Message:", '"""', text, '"""', sep="\n")
        
        # make the email object
        msg = MIMEText(text)
        msg['To'] = self.address
        msg['From'] = self.address
        msg['Subject'] = subject

        # log into the SMTP server to send it
        s = smtplib.SMTP(self.host, self.port)
        s.ehlo(); s.starttls()
        s.login(self.address, self.password)
        s.sendmail(self.address, [self.address], msg.as_string())
        s.quit()
        print("Sent!")
