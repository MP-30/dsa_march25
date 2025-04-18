import time
import threading


class numberPrinter(threading.Thread):
    
    def __init__(self, number):
        self.number = number
        threading.Thread.__init__(self)
        
    
    def run(self):
        
        print(f" Number is {self.number} printed by main thread is {threading.current_thread().name} and id is {threading.get_ident()}")
        time.sleep(1)
        