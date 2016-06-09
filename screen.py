import usercollection
import user
import RequestList
import PostList
import Post
import Request
import datetime
from PostList import PostList as P
import os
#from goto import goto, label

class screen:

    def __init__(self):
        self.user_list = usercollection.UserList()
        self.user_list.read()
        self.logged_in_user = None


    def mainScreen(self):
        print("__________________________________________")
        print("------------------------------------------")
        print("   Welcome to KD PARMAR's Facebook.....!!")
        print("------------------------------------------")
        print("------------------------------------------")
        option = -1
        while 1:
            print("1. Signup | " , end="")
            print("2. SignIn")
            print()
            option = input("Enter Input >> ")
            option = int(option)
            if option == 1:
                self.signup()
            elif option == 2:
                if self.loginScreen():
                    self.loginSuccess()

    def loginScreen(self):
        email =    input("Enter email    : ")
        password = input("Enter password : ")
        if self.user_list.login(email, password):
            self.logged_in_user = self.user_list.Ulist[email]
            return True
        print("Email or password mismatch !")
        return False

    def timeline(self):

        while 1:

            options_list = [' 1. Add a Post ',
                            ' 2. View All Posts ',
                            ' 3. Back ']

            for item in options_list:
                print(item, end="")

            option = int(input("Enter option"))

            if option is 1:
                content = input("Enter Contents: ")
                postcol = PostList.PostList()
                post    = Post.Post()
                post.content = content
                post.postBy  = self.logged_in_user
                post.today  = datetime.date.today()
                postcol.read()
                postcol.insert(post)
                postcol.write()

            elif option is 2:
                postcol = PostList.PostList()
                postcol.read()
                postcol.print_of_Friends(self.logged_in_user)
            elif option is 3:
                break


    def logout(self):
        self.logged_in_user = None
        return None

    def chat(self):
        pass
        #firnds list
        # 1.[ali (5)]
        # 2.[khan (1)]
        # 0 for search/send message to friend



    def help(self):
        help_list = [' 1. Chat '
                     ' 2. Friends '
                     ' 3. Log Out '
                     ' 4. Profile Update '
                     ]

        while 1:
            for item in help_list:
                print(" " + item + "  ", end="")
            option = int(input(" Enter option: "))

            if option is 1:
                self.chat()
            elif option is 2:
                self.firends()
            elif option is 3:
                self.logout()
                return -1
            elif option is 4:
                self.personal_profile()



    def firends(self):


        options = [' 1. Seach Users ',
                   ' 2. Print Requests ',
                   ' 3. Print Friends ']


        while 1:

            for option in options:
                print(option + " | ", end="")


            option = int(input("Enter Option: "))

            if option is 1:
                #Search USERS
                option = (input("Enter Username: "))
                ls = self.user_list.findByUsername(option)

                if ls:
                    counter = 1
                    for item in ls:
                        print(counter, item.UserName)
                        counter = counter + 1

                    request_option = int(input("Enter Option: "))
                    if request_option <= counter and request_option > 0:
                        print(" 1.Send Request ", end="")
                        print(" 2.cancel ", end="")

                        choice = int(input("Enter Option: "))
                        if choice == 1:
                            request = Request.Request()
                            request.ufrom = self.logged_in_user
                            request.uto   = ls[request_option-1]
                            request.today = datetime.date.today()

                            req_list = RequestList.RequestList()
                            req_list.read()
                            req_list.insert(request)
                            req_list.write()

            elif option is 2:
                req_list = RequestList.RequestList()
                req_list.read()
                ls = req_list.print_friend_reuests(self.logged_in_user.emailadd)
                if len(ls) > 1:
                    select_user_option = int (input("Enter option to accept request from: "))
                    acc_option = int(input("1. Accept, 2. Cancel: "))

                    if acc_option is 1:
                        ls[select_user_option-1].status = 1
                    else:
                        ls[select_user_option-1].status = -1

                    req_list.update(ls[select_user_option-1])
                    req_list.write()
            elif option is 3:
                req_list = RequestList.RequestList()
                req_list.read()
                req_list.print_friends(self.logged_in_user.emailadd)

        # friends list
        # 1 . request from ali
        ####### [1. Accept, 2. Reject]
        # 2 . request from ali
        ####### [1. Accept, 2. Reject]


    def footer(self):
        print("Logged in as: ", end="")
        print(self.logged_in_user.UserName + " | ", end="")

        print(" 1. Help ", end="")
        print(" 2. Chat ", end="")
        print(" 3. Friends ", end="")
        print(" 4. Post ", end="")
        print(" 5. Logout ", end="")

    def loginSuccess(self):
        while 1:
            self.timeline()
            self.footer()
            print("")
            option = int(input("Enter option: "))

            if option is 1:
                result = self.help()
                if result < 0:
                    return -1
            elif option is 2:
                self.chat()
            elif option is 3:
                self.firends()
            elif option is 4:
                self.timeline()
            elif option is 5:
                self.logout()
                os.system('cls')
                return -1

    def signup(self):

        u   = input("Enter username: ")
        e   = input("Enter email: ")
        p   = input("Enter password: ")

        fn  = input("Enter First Name: ")
        ln  = input("Enter Last Name: ")
        mn  = input("Enter Middle Name: ")

        dob = input("Enter DOB: ")

        u = user.FBUser()

        u.userName = u
        u.password = p
        u.dateofbirth = dob
        u.lastname = ln
        u.firstname = fn
        u.emailadd = e
        u.middlename = mn

        self.user_list.insert(u)

        self.user_list.write()



    def personal_profile(self):
        os.system('cls')
        self.Footer()
        me = usercollection.UserList.Ulist[self.usingPerson]
        print()
        print ('Name: ',me['firstname'],me['lastname'])
        print('Date Of Birth :',me['DateofBirth'])
        self.timeline()


    def MyFriendList(self):
        os.system('cls')
        #accessing through graph(not implemented yet)

    def RecievedRequest(self):
        os.system('cls')
        #accessing through graph(not implemented yet) those have status 0





