import os
# from django.core.mail import send_mail, send_mass_mail
import smtplib
import ssl

from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_MAIL = os.getenv("SMTP_MAIL")


class MAIL:
    """
    My SMTP MAIL CLASS
    """
    def __init__(self, SMTP_HOST:str, SMTP_USER:str, SMTP_PASS:str, SMTP_MAIL:str="test@test.com", SMTP_PORT:int=465) -> None:
        self.SMTP_HOST = SMTP_HOST
        self.SMTP_USERNAME = SMTP_USER
        self.SMTP_PASSWORD = SMTP_PASS
        self.SMTP_MAIL = SMTP_MAIL
        self.SMTP_PORT = SMTP_PORT

    def send_email(self, receiver, message: str) -> None:
        # try:
        #     smtpObj = smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT)
        #     smtpObj.login(user=SMTP_USERNAME, password=SMTP_PASSWORD)
        #     smtpObj.sendmail(sender, receivers, message)
        #     print("Successfully sent email")
        # except smtplib.SMTPException:
        #     # redirect user or output a beautiful message
        #     pass
        # finally:
        #     smtpObj.close()

        # Create a secure SSL context
        context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL(self.SMTP_HOST, self.SMTP_PORT, context=context) as server:
                server.login(self.SMTP_USERNAME, self.SMTP_PASSWORD)
                server.sendmail(self.SMTP_MAIL, receiver, message)
                print("Email sent...")
        except smtplib.SMTPException as e:
            print(e.strerror)
        finally:
            server.close()


mail_test = MAIL(SMTP_HOST=SMTP_HOST, SMTP_PORT=int(SMTP_PORT), SMTP_MAIL=SMTP_MAIL, SMTP_USER=SMTP_USERNAME, SMTP_PASS=SMTP_PASSWORD)
mail_test.send_email("cleffdawkins@gmail.com", "HELLO WORLD")
