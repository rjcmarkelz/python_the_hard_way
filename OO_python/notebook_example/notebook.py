import datetime

#store next available ID for all new notes
last_id = 0

class Note:
    '''Represent a note in a notebook. Match against a string
    in searches ans store tags for each note'''

    def __init__(self, memo, tags = ''):
        '''initialize a note with memo and optional
        space seperated tags'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''determine if this note matches'''
        return filter in self.memo or filter in self.tags


