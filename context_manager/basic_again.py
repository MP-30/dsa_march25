# with open('file.txt') as f:
#     data : str = f.read()
#     print(data)


import time

class Timer:
    def __new__(cls):
        pass
    
    def __init__(self, name :str) -> None:
        self.name = name
        
    def __enter__(self):
        self.start_time : float = time.time()
        print('Timer started')
        return self 
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time : float = time.time()
        print('Timer ended')
        return self
        

