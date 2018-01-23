
class Comment(object):
    

    def __init__(self, text, date):
        
        self.text = text
        self.date = date

    def __repr__(self):
        
        return "text: {}, date: {}".format(self.text, self.date)

COMMENTS = [('comment1','2018-01-21'),('comment2','2018-01-22'),('comment3','2017-01-23')]

