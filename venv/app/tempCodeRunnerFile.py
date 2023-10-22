from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuration for the MySQL connection
app.config['MYSQL_HOST'] = 'localhost'  # Replace with your MySQL host
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = '846004'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'personal_finance_manager'  # Replace with your MySQL database name

# Initialize MySQL
mysql = MySQL(app)

# Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userDetails = request.form
        username = userDetails['username']
        email = userDetails['email']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, email, password) VALUES(%s, %s, %s)", (username, email, password))
        mysql.connection.commit()
        cur.close()
        return 'Registration Successful'
    elif request.method == 'GET':
        return render_template('register.html')
    else:
        return 'Method Not Allowed'

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cur.fetchone()
        cur.close()

        if user:
            return "Login Successful"
        else:
            return "Invalid Credentials"
    elif request.method == 'GET':
        # Handle the GET request for login if required
        pass
    else:
        return 'Method Not Allowed'
