class Quote:
    '''
    Class for the received quote from quotes storm api
    '''
    def __init__(self,id, author,quote,permalink):
        '''
        Initializing quote variable
        '''
        self.id = id
        self.author = author
        self.quote = quote
        self.permalink = permalink