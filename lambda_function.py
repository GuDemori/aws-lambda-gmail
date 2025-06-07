import base64
import pickle
import os
from email.mime.text import MIMEText
from googleapiclient.discovery import build

def lambda_handler(event, context):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

    try:
        service = build('gmail', 'v1', credentials=creds)

        to = event.get('to', 'destinatario@gmail.com')
        subject = event.get('subject', 'Assunto de teste')
        body = event.get('body', 'Mensagem enviada pela AWS Lambda via Gmail API!')

        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject

        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        message_body = {'raw': raw_message}

        result = service.users().messages().send(userId='me', body=message_body).execute()
        return {'status': 'sucesso', 'id': result['id']}
    except Exception as e:
        return {'status': 'erro', 'mensagem': str(e)}