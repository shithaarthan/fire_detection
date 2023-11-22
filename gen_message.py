from twilio.rest import Client

def send_text_message():
    account_sid = 'ACd1bfad39d541804c236ffad442873777'
    auth_token = '5b534d415ecb17aa131ed150c6902d2e'
    twilio_phone_number = '+13203329020'
    recipient_phone_number = '+919965754127'
    message_body = 'Hello from Python!'
    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    # Send a text message
    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )

    return message.sid


message_sid = send_text_message()
print("Message SID:", message_sid)