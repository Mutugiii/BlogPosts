import unittest
from app.models import BlogPost
from app import db

class TestpostClass(unittest.TestCase):
    '''
    Test to test the post class/Table in db
    '''
    def setUp(self):
        '''
        To set up before each test case
        '''
        self.new_post = BlogPost(title = 'My post',content =  'I love this game')
        
    def tearDown(self):
        '''
        Function to clear up after every test case
        '''
        BlogPost.query.delete()

    def test_init(self):
        '''
        Test if variables are correctly initialzed
        '''
        self.assertEqual(self.new_post.title, 'My post')
        self.assertEqual(self.new_post.content, 'I love this game')

    def test_save_post(self):
        '''
        Test saving to test db
        '''
        self.new_post.save_post()
        self.assertTrue(len(post.query.all())>0)

