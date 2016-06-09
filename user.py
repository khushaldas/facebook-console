class FBUser:
    def __init__(self):
        self._firstname = ""
        self._userName = ""
        self._middlename = ""
        self._lastname = ""
        self._password = ""
        self._emailadd = ""
        self._dateofbirth = ""


    @property
    def UserName(self):
        return self._userName

    @UserName.setter
    def UserName(self, n1):
        self._userName = n1
    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, n1):
        self._firstname = n1

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, n2):
        self._lastname = n2

    @property
    def middlename(self):
        return self._middlename

    @middlename.setter
    def middlename(self, n3):
        self._middlename = n3

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, p):
        self._password = p

    @property
    def emailadd(self):
        return self._emailadd

    @emailadd.setter
    def emailadd(self, e):
        self._emailadd = e

    @property
    def dateofbirth(self):
        return self._dateofbirth

    @dateofbirth.setter
    def dateofbirth(self, d):
        self._dateofbirth = d

    @property
    def fathername(self):
        return self.fathername

    @fathername.setter
    def fathername(self, f):
        self.fathername = f

    def toJSON(self):
        return {'username': self._userName,'firstname': self._firstname,'middlename': self._middlename,
                'lastname': self._lastname,'emailadd': self._emailadd,'dateofbirth':self._dateofbirth,'password':self._password}
