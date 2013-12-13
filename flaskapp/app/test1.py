# -*- coding: utf-8 -*-
"""
    Flaskr Tests
    ~~~~~~~~~~~~

    Tests the Flaskr application.

    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import os
import routes
import unittest
import tempfile
import sqlite3 as lite



class FlaskrTestCase(unittest.TestCase):

       

    def login(self, Id, name):
        return self.app.post('/getstudent', data=dict(
            Id=Id,
            name=name
        ), follow_redirects=True)
   
    # testing functions

    def test_empty_db(self):
        """Start with a blank database."""
        rv = self.app.get('/')
        assert b'Welcome to Student databse' in rv.data

 

if __name__ == '__main__':
    unittest.main()

"""
   def test_login_logout(self):
      #  Make sure login and logout works
        rv = self.login(routes.app.config['ID'],
                        routes.app.config['NAME'])
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login(flaskr.app.config['USERNAME'] + 'x',
                        flaskr.app.config['PASSWORD'])
        assert 'Invalid username' in rv.data
        rv = self.login(flaskr.app.config['USERNAME'],
                        flaskr.app.config['PASSWORD'] + 'x')
        assert b'Invalid password' in rv.data

    def test_messages(self):
        #Test that messages work
        self.login(routes.app.config['ID'],
                   routes.app.config['NAME'])
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        assert b'No entries here so far' not in rv.data
        assert b'&lt;Hello&gt;' in rv.data
        assert b'<strong>HTML</strong> allowed here' in rv.data"""
