import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from decorator.time_deco import find_time

class UserDatabase:
    def __init__(self):
        self.users = [] 
     
    @find_time
    def insert(self, user):
        i = 0
        while i < len(self.users):
            if user.username < self.users[i].username:
                break
            i +=1
        self.users.insert(i, user)
    @find_time
    def find (self, username):
        for user in self.users:
            if user.username == username:
                return user

    @find_time
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
    @find_time    
    def remove(self, username):
        self.user.remove(self.find(username))
        
    @find_time
    def list_all(self):
        return self.users
        
class User: 
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = name
        
    def __repr__(self):
        return "User(username= '{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()
    
    
user1 = User('aditya', 'Aditya', 'aditya@example.com')
user2 = User('rohit', 'Rohit', 'rohit@example.com')
user3 = User('vivek', 'Vivek','vivek@mmail.com')
user4 = User('aditya', 'Aditya1', 'aditya@example.com')
database = UserDatabase()
user = database.insert(user1)
user = database.insert(user2)
user = database.insert(user3)
user = database.update(user4)



