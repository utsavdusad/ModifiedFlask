from flask import Flask, render_template, request
#from flask import *
import sqlite3 as lite

app = Flask(__name__)
app.config.from_object(__name__)



@app.route('/')
def homepage():
 return render_template('message.html',mssg="Welcome to Student databse")

@app.route('/getstudent/', methods=['GET'])
def test():
	con = None
	con = lite.connect('test.db')
	with con:	
		cur= con.cursor()		
		cur.execute('SELECT * from test')
		rows = cur.fetchall()	
		return render_template('hometest.html', rows=rows)

@app.route('/getstudent/<Id>', methods=['GET','POST'])
def show_user_profile(Id):
    # show the user profile for that user
    con = None
    con = lite.connect('test.db')

    with con:	

		cur= con.cursor()
		if request.method == 'GET':
			cur.execute('SELECT * from test where id='+ Id )
			rows = cur.fetchall()
			return render_template('hometest.html', rows=rows, Id = Id)
		elif request.method == 'POST':
			#cur.execute('insert into test (Id) values(' + Id+ ')' )			
			#cur.execute('insert into test values(' + Id+',"' +request.form['data'] + '")' )
			cur.execute('insert into test (Id,name) values(' + Id+',"' +request.form['data'] + '")' )

			return render_template('message.html',mssg="Data of ID=" + Id+  " name ="  + request.form['data'] + " entered successfully")
		cur.execute('SELECT * from test')
		rows = cur.fetchall()
		return render_template('hometest.html', rows=rows)

@app.route('/setstudent/<Id>/<name>',methods=['PUT','POST'])
def set_user_profile(Id,name):
    # show the user profile for that user
    con = None
    con = lite.connect('test.db')
    with con:	
		cur= con.cursor()
		if request.method == 'PUT':
			cur.execute('update test set Name="' + name + '"where id='+Id )
		elif request.method == 'POST':
			cur.execute('insert into test (Id,name) values(' + Id + ',"'+ name+'")' )
		cur.execute('SELECT * from test')
		rows = cur.fetchall()
		return render_template('hometest.html', rows=rows)
"""
@app.route('/setstudent/<Id>/<name>',methods=['POST'])
def new_user_profile(Id,name):
    # show the user profile for that user
    con = None
    con = lite.connect('test.db')
    with con:	
		cur= con.cursor()
		cur.execute('insert into test (Id,name) values(' + Id + ',"'+ name+'")' )
		cur.execute('SELECT * from test')
		rows = cur.fetchall()
		return render_template('hometest.html', rows=rows)
"""

  


"""
@app.route('/log', methods=['GET', 'POST'])
def log():
  error = None
  if request.method == 'POST':
    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
      error = 'Invalid Credentials. Please try again.'
    else:
      return redirect(url_for('hello'))
  return render_template('hello.html', error=error)
"""
if __name__ == '__main__':
#  init_db()
  app.run(debug=True)


