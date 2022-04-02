import os
from twilio.rest import Client
import smtplib


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_msg(self, body):
        account_sid = os.environ['ACC_SID']
        auth_token = os.environ['AUTH_TKN']

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=body,
            from_=os.environ['TWILIO_NUMBER'],
            to=os.environ['VerifiedNumber']
        )

        print(message.sid)

    def send_email(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.environ['EMAIL'], password=os.environ['PASS'])
            for email in emails:
                connection.sendmail(
                    from_addr=os.environ['EMAIL'],
                    to_addrs=email,
                    msg=message.encode('utf-8')
                    )
