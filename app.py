from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_mail import Mail, Message
import pybaseball
from datetime import datetime
import os

app = Flask(__name__)

# Use environment variables to keep your credentials secure
app.secret_key = os.getenv('SECRET_KEY')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tools')
def tools():
    return render_template('tools.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/got')
def got():
    return render_template('got.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/tutorials')
def tutorials():
    return render_template('tutorials.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


# Define the route for the login page
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/available_stats')
def available_stats():
    stats = pybaseball.batting_stats(2023)  # Example year, choose appropriately
    return jsonify(stats.columns.tolist())


@app.route('/player_dashboard')
def player_dashboard():
    return render_template('player_dashboard.html', selected_year=datetime.now().year)


@app.route('/filter_data', methods=['POST'])
def filter_data():
    data = request.json
    year = data['filters']['year']
    selected_stats = data['selectedStats']
    stats_data = pybaseball.batting_stats(year)
    print(stats_data.columns.tolist())  # This line will print the column names
    # Select only the requested stats
    filtered_data = stats_data[selected_stats]
    return jsonify(filtered_data.to_dict('records'))


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        subject = request.form['subject']
        email = request.form['email']
        message_body = request.form['message']
        msg = Message(subject, sender='hackingbaseball@gmail.com', recipients=['hackingbaseball@gmail.com'])
        msg.body = f"From: {email}\n\n{message_body}"
        mail.send(msg)
        flash('Email sent successfully!')
        return redirect(url_for('contact'))
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
