from flask import Flask, render_template
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '846004'
app.config['MYSQL_DB'] = 'personal_finance_manager'
mysql = MySQL(app)

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
        return 'success'
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)









if __name__ == '__main__':
    app.run(debug=True)
