import mail_sender.config as config
import requests

from .celery import app

@app.task
def send_email(id: int, from_name: str, to: list, subject: str, body: str):
    api_key = config.MAILGUN_KEY
    api_domain = config.MAILGUN_DOMAIN

    from_name_email = from_name.replace(" ", "")

    response = requests.post(
        f"https://api.mailgun.net/v3/{api_domain}/messages",
        auth= {"api", api_key},
        data = {
            "from" : f"{from_name} <{from_name_email}@{api_domain}>",
            "to" : to,
            "subject" : subject,
            "text" : body
        }
    )

    if response.status_code == 200:
        status = 'SE'
    else:
        status = 'FA'
    return requests.patch(
            config.DJANGO_URL + "email/" + str(id),
            data = {
                "status" : status
            }
        )
