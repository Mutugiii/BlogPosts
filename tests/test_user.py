import unittest
from app.models import User
from app import db

class TestUserModel(unittest.TestCase):
    '''
    Test class for the User Model
    '''
    
    def setUp(self):
        '''
        Function to prepare for every test case
        '''
        self.new_user = User(username='kamau', email='hellokamau@test.com', bio='This is a test bio', profile_pic_path='https://sites.google.com/site/dekchysite95/_/rsrc/1480944463347/extra-credit/google.png', password='kamau')

    def tearDown(self):
        '''
        Function to clear up after every test case
        '''
        User.query.delete()

    def test_init(self):
        '''
        Test if variables are correctly initialzed
        '''
        self.assertEqual(self.new_user.username, 'kamau')
        self.assertEqual(self.new_user.email, 'hellokamau@test.com')
        self.assertEqual(self.new_user.bio, 'This is a test bio')
        self.assertEqual(self.new_user.profile_pic_path, 'https://sites.google.com/site/dekchysite95/_/rsrc/1480944463347/extra-credit/google.png')
        
    def test_save_user(self):
        '''
        Test saving to test db
        '''
        self.new_user.save_user()
        self.assertTrue(len(User.query.all())>0)


    def test_password_setter(self):
        '''
        Test that the password setter works
        '''
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        '''
        Confirm that attribute error is raised when we try to access password attrib
        '''
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        '''
        Test the verify_password function
        '''
self.assertTrue(self.new_user.verify_password('kamau'))