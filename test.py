

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC61b5962310dbcd5cd22542043d9e657e"
# Your Auth Token from twilio.com/console
auth_token  = "b8ce06b367327840287e7f8c35b27c16"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18024983534", 
    from_="+13363447244",
    body="Hello from Python!")

print(message.sid)