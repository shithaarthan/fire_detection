from twilio.rest import Client

def send_text_message():
    account = 'your twilio account sid'
    auth_token = 'your auth_token from twilio'
    twilio_phone_number = 'your twilio phone number'
    recipient_phone_number = 'reciver phone number'
    message_body = 'Hello fire alert!'
    # Initialize Twilio client
    client = Client(account, auth_token)

    # Send a text message
    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )

    return message.sid


