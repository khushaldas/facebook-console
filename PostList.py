from Post import Post as P
from paths import  BASE_PATH
import  user
import  usercollection
import RequestList
import datetime
import  json
class PostList:

    def __init__(self):
        self.LPost= {}

    def insert(self,post):
        self.LPost[post.id] =  post

    def print(self,user):

        for item in self.LPost.keys():

            if self.LPost[item].postBy.emailadd == user.emailadd:
                print('------------------')
                print("Post BY: ", self.LPost[item].postBy.UserName)
                print(self.LPost[item].content)
                print('------------------')


    def print_all(self):
        for item in self.LPost.keys():
            print('------------------')
            print("Post BY: ", self.LPost[item].postBy.UserName)
            print(self.LPost[item].content)
            print('------------------')

    def print_of_Friends(self,user):
          u = RequestList.RequestList()
          u.read()
          ls = u.get_friends(user.emailadd)
          ls.append(user)
          print(ls)
          for item in ls:
              self.print(item)

    def toJSON(self):
        temp = self.LPost.copy()
        temp2 = self.LPost.copy()
        for key in temp.keys():
            temp2[key] = temp[key].toJSON()
        return temp2


    def write(self):
        with open(BASE_PATH + "post.list.data.txt", 'w') as f:
            json.dump(self.toJSON(), f)


    def read(self):
         with open(BASE_PATH+"post.list.data.txt",'r+') as f:
            l = json.load(f)

            for key in l.keys():
                item = l[key]

                p = P()
                u = usercollection.UserList()
                u.read()
                p.postBy = u.findByString(item['postBy'])
                p.content = item['content']
                p.today =  datetime.datetime.strptime(item['today'], "%m/%d/%Y")
                p.likes = item['likes']

                self.insert(p)
