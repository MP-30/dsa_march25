'''
as a senior backend engineer at jovian, you are tasked with developing a fast in
memory data structure to manage profile information (username, name, email) for 100 million users.
It should allow the following operations to be performed efficiently:
1. Insert
2. Find
3. Update
4. List
'''


class UserDatabase:
    def __init__(self):
        self.users = []
    def insert(self, user):
        i = 0
        while i < len(self.users):
            if user.username < self.users[i].username:
                break
            i +=1
        self.users.insert(i,user)
        
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
        
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        
    def remove(self,username):
        target = self.find(username)
        self.users.remove(target)
        
    def list_all(self):
        return self.user

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f"User (username={self.username}, name = {self.name}, email = {self.email})"

    def __str__(self):
        return self.__repr__()
    
    
aditya = User(username='aditya', name='Aditya Singh', email='aditya@gmail.com')
rohit = User(username='rohit', name='Rohit Singh', email='rohit@gmail.com')
vivek = User(username='vivek', name='Vivek Kumar', email='vivek@gmail.com')
vinayak = User(username='vinayak', name='Vinayak Kumar', email='vinayak@gmail.com')
pinky = User(username='pinky', name='Pinky Kumari', email='pinky@gmail.com')
rahul = User(username='rahul', name='Rahul Kumar', email='rahul@gmail.com')

users = [aditya, rohit, vivek, vinayak, pinky, rahul]

database = UserDatabase()
database.insertion(aditya)
database.insertion(rohit)
database.insertion(vinayak)
database.insertion(vivek)
database.insertion(pinky)
database.insertion(rahul)

database.update(User(username='aditya', name='aditya singh bhadauriya', email='aditya1@gmail.com'))
# print(database.list_all())
print(database.find('rahul'))
print(database.find('aditya'))

# print(type(aditya))
# print(aditya)

