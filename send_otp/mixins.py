from twilio.rest import Client
from django.conf import settings



class MessHandler:
    def sent_otp_number(phone_number=None, otp=None):
        phone_number =  phone_number
        otp = otp 

        client =   Client(settings.ACCOUNT_SID , settings.AUTH_TOKEN)
        message = client.messages.create(                               
                    body =  f'Your otp is {otp}',
                    from_ = '' ,      # activate number
                    to_ =  phone_number
                )
        print(message)


