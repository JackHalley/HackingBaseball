from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "some_secret_key"  # Change this to your secret key

# Configurations for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'YOUR_EMAIL@gmail.com'
app.config['MAIL_PASSWORD'] = 'YOUR_PASSWORD'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        subject = request.form['subject']
        email = request.form['email']
        message_body = request.form['message']

        msg = Message(subject, sender=email, recipients=['YOUR_EMAIL@gmail.com'])
        msg.body = message_body
        mail.send(msg)

        flash('Email sent successfully!')
        return redirect(url_for('contact'))

    return render_template('contact.html')


if __name__ == "__main__":
    app.run()
