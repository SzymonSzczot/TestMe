from mailjet_rest import Client

from django.template.loader import render_to_string, get_template
from config import settings
from tools.tools import EmailException


class EmailSender:
    def __init__(self, data):
        self.client_id = settings.EMAIL_ID
        self.client_secret = settings.EMAIL_SECRET
        self.email_from = settings.EMAIL_FROM
        self.data = data

    def authenticate_user(self):
        return Client(
            auth=(self.client_id, self.client_secret),
            version='v3.1'
        )

    def prepare_email_template(self, template_name):
        template = get_template(template_name)
        return template.render(self.data)

    def prepare_email(self):
        return {
            'Messages': [
                {
                    "From": {
                        "Email": "hubertjan98@gmail.com",
                        "Name": "Hubert"
                    },
                    "To": [
                        {
                            "Email": f"{self.data['email_to']}",
                            "Name": f"{self.data['user_first_name']}"
                        }
                    ],
                    "Subject": f"{self.data['subject']}",
                    "HTMLPart": self.prepare_email_template('reset_password.html'),
                }
            ]
        }

    def send_email(self):
        response = self.authenticate_user().send.create(data=self.prepare_email())
        if response.status_code != 200:
            raise EmailException()
        else:
            return response
