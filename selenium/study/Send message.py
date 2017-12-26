# coding:utf-8
from twilio.rest import Client;
ACCOUNT_SID = "AC2d4271634bfd45a88061e2d3d552d462"    #ly
AUTH_TOKEN = "59f2072bdf5701544fa8c19e1dc305d8"      #ly
client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages.create(
        body="You are the best!",
        # to="+8617720546681",  #在网站验证的sim卡号
        to="+8618062427385",  #在网站验证的sim卡号
        from_="+13368037446"   #网站虚拟的一个卡号
)
print(message.sid)