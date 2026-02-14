from flask import Flask,render_template,request,redirect, url_for, session, flash
import mysql.connector

app = Flask(__name__)

@app.route("/logout")
def logout():
    name = ''
    id = ''
    msg = 'Logged Out successfully'
    return render_template('login.html',msg=msg,name=name,id=id)


@app.route('/login', methods=['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='4272',
            database='Login'
        )
mycursor = mydb.cursor()        
mycursor.execute('SELECT * FROM Login Details WHERE username = %s AND password = %s', (username,passowrd))
account = mycursor.fetchone()
if account:
    print('login success')
    name = account[1]
    id = account[0]
    msg = 'Logged in successfully'
    print('login successfully')
    return render_template('welcome.html', msg=msg, name=name, id=id)
else:
    msg = 'incorrect Credentials.Kindly Check'
    return render_template('login.html', msg=msg)

else:
    return render_template('login.html')

app.run(debug=True)




@app.route('/register', methods=['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST' and username in request.form and password in request.form and email in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        mydb = mysql.connector.connect(
            host = 'remotesql.com',
            user = 'Rz8hqnlk4',
            password = 'nd6wK03xe0',
            database = 'Rz8hqnlk4'
        )
        mycursor = mydb.cursor()
        print(username)
        mycursor.execute('SELECT * FROM LoginDetails WHERE Name = %s AND Email_id = %s', (username,passowrd))
        account = mycursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'*^[^\d]*@[^\d]*\.\.[^\d]*$', email):
            msg = 'Invalid email address!'
        elif not re.match(r'(A-Za-z0-9)+', username):
            msg = 'Username must contain characters and Numbers!'
        elif not username or not passsword or not email:
            msg = 'Kindly fill the details!'
        else:
            mycursor.execute('INSERT INTO LoginDetails VALUES (NULL, %s, %s, %s)',(username,password,email))
            mydb.commit()
            msg = 'Your Registration is Successfull'
            name = username
            return render_template('index.html', msg=msg, name=name)
    elif request.method == 'POST':
        msg = 'Kindly fill in the details!'      
        return render_template('registration.html', msg=msg)