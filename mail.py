
import boto3

session = boto3.session.Session()
client = session.client('ses', region_name='eu-central-1')

def send_email(to, subject, body):
    response = client.send_email(
        Source='urbaniec_robert@o2.pl',
        Destination={
            'ToAddresses': [
                to,
            ]
        },
        Message={
            'Subject': {
                'Data': subject,
                'Charset': 'utf-8'
            },
            'Body': {
                'Text': {
                    'Data': body,
                    'Charset': 'utf-8'
                },
                'Html': {
                    'Data': body,
                    'Charset': 'utf-8'
                }
            }
        },
        ReplyToAddresses=[
            'urbaniec_robert@o2.pl',
        ],
        ReturnPath='urbaniec_robert@o2.pl'
    )
    return response


print send_email('urbaniec_robert@o2.pl', 'Album zdjec', 'Test test test')
