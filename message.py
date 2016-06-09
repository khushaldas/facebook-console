import datetime
class msg:

    def __init__(self):
        self.msgTo
        self.msgFrom
        self.msg = ""
        self.seenStatus = 0
        self.today = datetime.date.today()

    @property
    def today(self):
        return self.today

    @today.setter
    def today(self, t):
        t = datetime.date.today()
        self.today = t

    @property
    def msgTo(self):
        return self.msgTo

    @msgTo.setter
    def msgTo(self,u1):
        self.msgTo=u

    @property
    def msgFrom(self):
        return  self.msgFrom

    @msgFrom.setter
    def msgFrom(self,u2):
        self.msgFrom = u2

    @property
    def msg(self):
        return self.msg

    @msg.setter
    def msg(self,m):
        self.msg = msg

    @property
    def seenStatus(self):
        return self.seenStatus

    @seenStatus.setter
    def seenStatus(self):
        self.seenStatus = 1

    def toJSON(self):
        return {'UFrom': self.UFrom, 'Uto': self.UTo,'Msg':self.msg,'status':self.seenStatus}
