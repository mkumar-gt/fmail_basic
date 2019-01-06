from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)
import os


app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.environ['MAIL_USERNAME'],
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
))

mail = Mail(app)


@app.route("/")
def index():

	msg = Message("Hello Mu",
		sender="muthukumar.nf@gmail.com",
		recipients=["muth_ukumar@yahoo.com"]
		)
	msg.body = "Just testing my psend2 app"

	mail.send(msg)

	return 'Mail send was attempted'