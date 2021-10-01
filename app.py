from getpass import getpass
from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = getpass('Enter your username: ') # This will be asked twice ('replace')
app.config['MYSQL_PASSWORD'] = getpass('Enter the main password: ') # This will be asked twice (replace)
app.config['MYSQL_DB'] = 'password_manager'

mysql = MySQL(app)


# Routes
# Get all logins for home page
@app.route('/')
@app.route('/home')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM login')
    data = cur.fetchall()
    return render_template('home.html', data=data)


# Post/Create new login
@app.route('/add_login', methods=['POST'])
def add_login():
    if(request.method == 'POST'):
        name = request.form['name']
        user = request.form['user']
        password = request.form['password']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO login(name, user, password, email) VALUES (%s, %s, %s, %s)', (name, user, password, email))
        mysql.connection.commit()

        return redirect('/')

# Get login details on a new page
@app.route('/login/<id>', methods=['GET'])
def get_login(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM login WHERE id=%s', (id,))
    data =cur.fetchall()

    return render_template('details.html', data=data)

#Update login details function
@app.route('/login/update/<id>', methods=['GET', 'POST'])
def update_login(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM login WHERE id=%s', (id))
    data = cur.fetchall()

    if(request.method == 'POST'):
        name = request.form['name']
        user = request.form['user']
        password = request.form['password']
        email = request.form['email']

        cur.execute('UPDATE login SET name=%s, user=%s, password=%s, email=%s WHERE id=%s', (name, user, password, email, id))
        mysql.connection.commit()
        
        return redirect(url_for('get_login', id=id))
    
    return render_template('update.html', data=data)


# Delete login details
@app.route('/login/delete/<id>')
def delete_login(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM login WHERE id=%s', (id,))
    mysql.connection.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
