

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "xxxxxxxxxxxxxxxxxxxxx"
# Your Auth Token from twilio.com/console
auth_token  = "yyyyyyyyyyyyyyyyyyyyy"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12345874587", 
    from_="+13363447244",
    body="Hello from Python!")

print(message.sid)
