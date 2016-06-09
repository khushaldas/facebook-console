from user import FBUser as User
import json
from paths import BASE_PATH
class UserList:
    Ulist = {}

    def insert(self, User):
        if (User.emailadd) in self.Ulist :
            return False
        else:
            self.Ulist[User.emailadd]=User

    def Update(self,User):
        if (User.emailadd) in self.Ulist :
            self.Ulist[User.emailadd] = User
        else:
            return False

    def delete(self,User):
        if (User.emailadd) in self.Ulist :
            del self.Ulist[User.emailadd]

    def find(self,User):
        if (User.emailadd) in self.Ulist :
            return User
        else:
            return False

    def findByString(self,string):
        if string in self.Ulist :
            return self.Ulist[string]
        else:
            return None

    def findByUsername(self,username):
        filtered = []
        for key in self.Ulist.keys():
            item = self.Ulist[key]
            if item.UserName.lower().find(username.lower()) > -1:
                filtered.append(item)
        return filtered

    def print_collection(self):
        for item in self.Ulist:
            print(item)
    def toJSON(self):
        temp  = self.Ulist.copy()
        temp2 = self.Ulist.copy()
        for key in temp.keys():
            temp2[key] = temp[key].toJSON()
        return temp2
        
    def write(self):
        with open(BASE_PATH+"users.list.data.txt", 'w') as f:
            json.dump(self.toJSON(), f)

    def login(self, email, password):

        if email in self.Ulist:
            if self.Ulist[email].password == password:
                return True
            return False
        else:
            return None

    def read(self):
        with open(BASE_PATH+"users.list.data.txt",'r') as f:
            l = json.load(f)
            for key in l.keys():
                item = l[key]

                u = User()
                u.UserName = item['username']
                u.firstname = item['firstname']
                u.lastname = item['lastname']
                u.middlename = item['middlename']
                u.emailadd = item['emailadd']
                u.password = item['password']
                u.dateofbirth = item['dateofbirth']
                self.Ulist[u.emailadd] = u
