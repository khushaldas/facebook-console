from message import msg as m
import json
class msgList:

    def __init__(self):
        self.mList = {}

    def SendMsg(self,msg):
        pass

    def deleteMsg(self):
        pass

    def FindMsg(self):
        pass

    def toJSON(self):
        temp  = self.mList.copy()
        temp2 = self.mList.copy()
        for key in temp.keys():
            temp2[key] = temp[key].toJSON()
        return temp2

    def write(self):
        with open("msg.list.data.txt", 'w') as f:
            json.dump(self.toJSON(), f)

    def read(self):
        with open("msg.list.data.txt", 'r') as f:
            self.RList = json.load(f)