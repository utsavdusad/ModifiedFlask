from flask.ext.testing import TestCase
class Mytest(TestCase):

	
	def create_app(self):
		app = Flask(__name__)
 		app.config['TESTING'] = True
        	return app
	
	

	
