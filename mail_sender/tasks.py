import mail_sender.config as config
import requests

from .celery import app

@app.task
def send_email(id: int, from_name: str, to: list, subject: str, body: str, api_key: str, api_domain: str):
    trace_log = []

    from_name_email = from_name.replace(" ", "")

    print(to)
    trace_log.append(to)

    response = requests.post(
        f"https://api.mailgun.net/v3/{api_domain}/messages",
        auth= ("api", api_key),
        data = {
            "from" : f"{from_name} <{from_name_email}@{api_domain}>",
            "to" : to,
            "subject" : subject,
            "text" : body
        }
    )
    
    print(response.text)
    trace_log.append(response.text)

    if response.status_code == 200:
        status = 'SE'
    else:
        status = 'FA'

    print(status)
    trace_log.append(status)

    response = requests.patch(
        config.DJANGO_URL + "email/" + str(id),
        json = {
            "status" : status
        }
    )

    print(response.text)
    trace_log.append(response.text)

    return trace_log

