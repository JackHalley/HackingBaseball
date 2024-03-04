from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db_connection():
    connection = sqlite3.connect('lpDatabase.db')
    connection.row_factory = sqlite3.Row
    return connection

# Function to create the users table if it doesn't exist
def create_users_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
        first_name TEXT,
        last_name TEXT,
        email TEXT
        )
    ''')
    connection.commit()
    connection.close()
    print("Users table created successfully.")  # Print a message to the console

# Function to insert sample data into the database for testing
# def insert_sample_data():
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO users (first_name, last_name, email) VALUES (?, ?, ?)", ('Jack', 'Does', 'john@example.com'))
#     cursor.execute("INSERT INTO users (first_name, last_name, email) VALUES (?, ?, ?)", ('Bek', 'Wants', 'jane@example.com'))
#     connection.commit()
#     connection.close()
#     print("Sample data inserted successfully.")  # Print a message to the console

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        
        # Insert user data into the database
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (first_name, last_name, email) VALUES (?, ?, ?)", (first_name, last_name, email))
        connection.commit()
        connection.close()
        
        return "User data submitted successfully."

if __name__ == "__main__":
    create_users_table()  # Create users table if it doesn't exist
    # insert_sample_data()  # Insert sample data into the database for testing
    print("Starting Flask app...")  # Print a message to the console
    app.run(port=5001, debug=True)  # Change the port number to 5001 or any other available port
