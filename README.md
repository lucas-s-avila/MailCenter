# MailCenter
This application can handle the sending of emails for multiples destinations and monitoring the status of them.

It uses the [MailGun API](www.mailgun.com) to send the emails and trace it.

## How to setup
Before running, you can configure some variables in `docker/variables.env` to your personal use. Although you can run with the default variables in it.

To execute the application, just go under the `docker` folder and run:

``` bash
cd docker
docker-compose up -d
```

And you can go to `http://localhost:5000/admin` to see it running.

![image](https://user-images.githubusercontent.com/21691078/137667835-c6366e70-69ef-421c-9579-6441feb2900e.png)


## How to use
As you have to set an API key and domain for start sending emails via MailGun, first you have to create an account where you set a name (which will got as the sender name on the email), a domain and a key.

![image](https://user-images.githubusercontent.com/21691078/137667404-0814c305-3994-4c22-afb9-7d3cabf91b5a.png)

Then you can create an email, selecting an account and fill in the subject, receivers (one per line) and body of the message.

![image](https://user-images.githubusercontent.com/21691078/137667445-9178f802-6a8f-4e7d-8ca6-7363a3340c51.png)

When you return to the email list page, you can check its status.

![image](https://user-images.githubusercontent.com/21691078/137667810-b07dffe6-1901-4df3-86ff-efbdb4b9b47e.png)
