from user import FBUser as user
import datetime

class Request:

    def __init__(self):
        self._ufrom = None
        self._uto = None
        self._status = 0
        self._today = datetime.date.today()

    @property
    def ufrom(self):
        return self._ufrom

    @ufrom.setter
    def ufrom(self,U1):
        self._ufrom = U1

    @property
    def uto(self):
        return self._uto

    @uto.setter
    def uto(self,U2):
        self._uto = U2

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,s):
        self._status = s

    @property
    def today(self):
        return  self._today

    @today.setter
    def today(self,t):
        self._today = t

    def toJSON(self):
        return {'ufrom': self._ufrom.emailadd, 'uto': self._uto.emailadd,'status':self._status,'today':self._today.strftime('%m/%d/%Y')}
