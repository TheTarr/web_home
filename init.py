from flask import Flask, render_template, request, url_for, redirect, session
import mysql.connector

#Initialize the app from Flask
app = Flask(__name__)

# #Configure MySQL
# conn = mysql.connector.connect(host='localhost',
#                                user='mlatus',
#                                password='pass',
#                                database='flight')

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/index.html')
def hello_again():
    return render_template('index.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/about_us.html')
def about_us():
    return render_template('about_us.html')

@app.route('/about_me.html')
def about_me():
    return render_template('about_me.html')

@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
    inlineRadioOptions = request.form['inlineRadioOptions']
    if inlineRadioOptions != '1':
		#If the previous query returns data, then user exists
        error = "您居然不是人？！很好啊……但是注册这回事确实是骗人的啦！"
        return render_template('index.html', error = error)
    else:
        error = '注册这回事真的是骗人的啦！'
        return render_template('index.html', error = error)

	# #cursor used to send queries
	# cursor = conn.cursor()
	# #executes query
	# query = "SELECT * FROM user WHERE username = '{}'"
	# cursor.execute(query.format(username))
	# #stores the results in a variable
	# data = cursor.fetchone()
	# #use fetchall() if you are expecting more than 1 data row
	# error = None
	# if(data):
	# 	#If the previous query returns data, then user exists
	# 	error = "This user already exists"
	# 	return render_template('register.html', error = error)
	# else:
	# 	ins = "INSERT INTO user VALUES('{}', '{}')"
	# 	cursor.execute(ins.format(username, password))
	# 	conn.commit()
	# 	cursor.close()
	# 	return render_template('index.html')


app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION

if __name__ == "__main__":
    app.run('127.0.0.1', 3000, debug=True)
