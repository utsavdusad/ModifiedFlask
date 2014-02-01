import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = 'routestemp.db'
DEBUG = True
app = Flask(__name__)
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)


app.config.from_object(__name__)

"""def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
"""

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    
    return rv


def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

"""
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
"""
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.before_request
def before_request():
    g.db = connect_db()

"""@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
"""
@app.route('/')
def homepage():
 return render_template('message.html',mssg="Welcome to Student databse")




@app.route('/getstudent/', methods=['GET'])
def test():
	#print "my name is khan"	
	cur = g.db.execute('select * from student')		
	#rows = [dict(Id=row[0], name=row[1]) for row in cur.fetchall()]
	rows = cur.fetchall()
	return render_template('hometest.html', rows=rows)
	#return render_template('hometest.html')	

@app.route('/getstudent/<Id>', methods=['GET','POST'])
def show_user_profile(Id):
    # show the user profile for that user
    #print "my name is khan"	
    if request.method == 'POST':
	#db = get_db()
    	#g.db.execute('insert into student (id,name) values("' + Id+'","' +request.form['data'] + '")' )
    	g.db.execute('insert into student (id, name) values (?, ?)',
                 [Id, request.form['data']])
	g.db.commit()	
	return render_template('message.html',mssg="Data of ID=" + Id+  " name ="  + request.form['data'] + " entered successfully")
    elif request.method == 'GET':
    	cur=g.db.execute('select * from student where id='+ Id)
    	#entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
	#cur=g.db.execute('select * from student where id='+ Id)	
	entries = cur.fetchall()
	return render_template('hometest.html', mssg='Yes', rows=entries, Id = Id)
    
    return redirect(url_for('test'))

@app.route('/setstudent/<Id>/<name>',methods=['PUT','POST'])
def set_user_profile(Id,name):
    # show the user profile for that user
#    con = None
#   con = lite.connect('test.db')
#    with con:	
#		cur= con.cursor()
		if request.method == 'PUT':
			cur=g.db.execute('update student set Name="' + name + '"where id='+Id )
		elif request.method == 'POST':
			g.db.execute('insert into student (Id,name) values(' + Id + ',"'+ name+'")' )
		cur=g.db.execute('SELECT * from student')
		rows = cur.fetchall()
		return render_template('hometest.html', rows=rows)

@app.route('/deletestudent/<Id>',methods=['DELETE'])
def delete_user_profile(Id):
    
		cur=g.db.execute('delete from student where id='+Id )
		cur=g.db.execute('SELECT * from student')
		rows = cur.fetchall()
		return render_template('hometest.html', rows=rows)
  


if __name__ == '__main__':
  init_db()
  app.run(debug=True)


