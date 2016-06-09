from user import FBUser as user
from like import Like as l
from random import randint
import datetime

class Post:
    def __init__(self):
        self._id = int(randint(123,123245))
        self._content = ""
        self._today = datetime.date.today()
        self._likes = []
        self._postBy= None

    @property
    def postBy(self):
        return  self._postBy
    @postBy.setter
    def postBy(self,i):
        self._postBy = i
    @property
    def id(self):
        return  self._id
    @id.setter
    def id(self,i):

        i = random(567,123467)
        print(i)
        self._id = i

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self,c):
        self._content = c

    @property
    def today(self):
        return self._today

    @today.setter
    def today(self,t):
        t = datetime.date.today()
        self._today = t

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, like):
        self._likes.append(like)


    def toJSON(self):
        return {'id': self._id, 'content': self._content,'postBy':self._postBy.emailadd,'today':self._today.strftime('%m/%d/%Y'),'likes':self._likes}