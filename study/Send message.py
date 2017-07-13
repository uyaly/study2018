# coding:utf-8
from twilio.rest import Client;
ACCOUNT_SID = "AC2d4271634bfd45a88061e2d3d552d462"
AUTH_TOKEN = "59f2072bdf5701544fa8c19e1dc305d8"
client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages.create(
        body="You are the best!",
        to="+8617720546681",   # Replace with your phone number
        from_="+ 13368037446"
)
print(message.sid)