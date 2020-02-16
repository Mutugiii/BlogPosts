import urllib.request, json
from .models import Quote

# Getting the API URL
api_url = None

def configure_request(app):
    '''
    Create application instance as app can't be globally accessed
    '''
    global api_url
    api_url = app.config['API_URL']

def get_quote():
    '''
    Function to make the api call and return the request object
    '''
    quote_return = json.loads(urllib.request.urlopen(api_url).read())

    quote_object = None
    if quote_return:
        id = quote_return.get('id')
        author = quote_return.get('author')
        quote = quote_return.get('quote')
        permalink = quote_return.get('permalink')

        quote_object = Quote(id, author, quote, permalink)

    return quote_object

