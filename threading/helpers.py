import time
import threading

def dosomething(person_name):
    print(f'done some thingh {person_name}')
    print(f"main thread is {threading.current_thread().name} and id is {threading.get_ident()}")
    time.sleep(1)
    print(f'doing some thingh {person_name}')
    
    
class Dosomething(threading.Thread):
    
    
    def __init__(self, person_name):
        self.person_name = person_name
        threading.Thread.__init__(self)
    
    def run(self):
        print(f'done some thingh {self.person_name} ')
        print(f"main thread is {threading.current_thread().name} and id is {threading.get_ident()}")
        time.sleep(1)
        print(f'doing some thingh {self.person_name}')