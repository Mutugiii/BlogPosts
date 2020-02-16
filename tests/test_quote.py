import unittest
from app.models import Quote

class TestQuote(unittest.TestCase):
    '''
    Test class to test the random quote received from the quotes storm api
    '''
    def setUp(self):
        '''
        Function to set up for every test case
        '''
        self.new_quote(2, 'Edward van Gogh', 'Hii maisha haitaki makasiriko', "http://quotes.stormconsultancy.co.uk/quotes/2")

    def tearDown(self):
        '''
        To clean up after every test case
        '''
        self.new_quote = None

    def test_init(self):
        '''
        Test correct initialization
        '''
        self.assertEqual(self.new_quote.id, 2)
        self.assertEqual(self.new_quote.author, 'Edward van Gogh')
        self.assertEqual(self.new_quote.quote, 'Hii maisha haitaki makasiriko')
        self.assertEqual(self.new_quote.permalink, "http://quotes.stormconsultancy.co.uk/quotes/2")

    def test_instance(self):
        '''
        Test if it is instance of the parent class
        '''
        self.assertTrue(isinstance(self.new_quote, Quote))