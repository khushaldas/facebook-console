from Request import Request
import  usercollection
import  datetime
from paths import BASE_PATH
import json

class RequestList:
    def __init__(self):
        self.RList = {}

    def insert(self, req):

        if (req.uto.emailadd) in self.RList :
            if req.ufrom.emailadd in self.RList[req.uto.emailadd]:
                return False
            else:
                self.RList[req.uto.emailadd][req.ufrom] = req

        else:
            self.RList[req.uto.emailadd]={req.ufrom.emailadd:req}

    def update(self, req):
        if (req.uto.emailadd) in self.RList :
            if req.ufrom.emailadd in self.RList[req.uto.emailadd]:
                print("UPDATING .... ")
                self.RList[req.uto.emailadd][req.ufrom.emailadd] = req

    def acceptRequest(self,user):
        if user.email in self.RList:
            return False
        self.RList[user.email] = user

    def deleteRequest(self,user):
        if user.email in self.RList:
            del self.RList[user.email]
            return  True
        else:
            return False

    def FindFriend(self,user):
        if user.email in self.RList:
            return True
        else:
            return False
    def print_friend_reuests(self, email):
        R=[]
        if email in self.RList:
            counter = 1
            for key in self.RList[email]:
                item = self.RList[email][key]
                if item.status in [0, -1]:
                    print(counter, " " ,item.toJSON())
                    R.append(item)
                    counter = counter + 1
        return  R


    def print_friends(self, email):
        R=[]
        counter = 1
        if email in self.RList:

            for key in self.RList[email]:
                item = self.RList[email][key]
                if item.status is 1:
                    print(counter, " " ,item.toJSON())
                    R.append(item)
                    counter = counter + 1


        for k in self.RList:
            if email in self.RList[k]:
                item = self.RList[k][email]
                if item.status is 1:
                    print(counter, " " ,item.toJSON())
                    R.append(item)
                    counter = counter + 1


        return  R
    def get_friends(self, email):
        R=[]
        counter = 1
        if email in self.RList:

            for key in self.RList[email]:
                item = self.RList[email][key]
                if item.status is 1:
                    R.append(item.ufrom)


        for k in self.RList:
            if email in self.RList[k]:
                item = self.RList[k][email]
                if item.status is 1:
                    R.append(item.uto)
                    counter = counter + 1


        return  R

    def toJSON(self):
        print(self.RList)
        temp  = self.RList.copy()
        temp2 = self.RList.copy()
        for key in temp.keys():
            for key2 in temp[key].keys():
                temp2[key][key2] = temp[key][key2].toJSON()
        return temp2

    def write(self):
        with open(BASE_PATH+"request.list.data.txt", 'w') as f:
            json.dump(self.toJSON(), f)

    def read(self):
        with open(BASE_PATH+"request.list.data.txt", 'r+') as f:
            l = json.load(f)
            for key in l.keys():
                for key2 in l[key].keys():
                    item = l[key][key2]
                    R = Request()
                    u = usercollection.UserList()
                    u.read()
                    R.ufrom = u.findByString(item['ufrom'])
                    R.uto = u.findByString(item['uto'])
                    R.status = item['status']
                    R.today = datetime.datetime.strptime(item['today'], "%m/%d/%Y")

                    self.insert(R)

