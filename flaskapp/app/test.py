import unittest
import tempfile
import routestemp
import os
class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, routestemp.app.config['DATABASE'] = tempfile.mkstemp()
	#self.db_fd, routestemp.app.config['DATABASE'] = 'routestemp.db'        
	self.app = routestemp.app.test_client()
        routestemp.init_db()

    def tearDown(self):
	#pass        
	os.close(self.db_fd)
        os.unlink(routestemp.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'Welcome' in rv.data

    def get_add(self):	
	return self.app.get('/getstudent/1')
   
    def test_get_add(self):
    	rv=self.get_add()        
	assert  'Yes' in rv.data


    def post_add(self,data):
    	return self.app.post('/getstudent/9', data={'data':data})

   
    def test_post_add(self):
	rv=self.post_add('Mayur')        
	#assert 'entered successfully' in rv.data
	assert  '400 Bad Request' in rv.data
   

    def put_add(self):
	return self.app.put('/setstudent/1/Mayur')

    def test_put_add(self):
	rv=self.put_add()
	assert '400 Bad Request' in rv.data	

    def delete_user(self):
	return self.app.delete('/deletestudent/1')

    def test_delete_user(self):
	rv=self.delete_user()
	assert '400 Bad Request' in rv.data	
    
if __name__ == '__main__':
    unittest.main()
