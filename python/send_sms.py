from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8912ff2c5411e601bb36baf246423e79"
# Your Auth Token from twilio.com/console
auth_token  = "9c77cd1135ec4e42c2be54192ff80d42"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8618990166352", 
    from_="+14243836768 ",
    body="Hello from Kat!")

print(message.sid)
