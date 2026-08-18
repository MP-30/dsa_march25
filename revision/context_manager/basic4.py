from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:    
        f.close()

with open_file('sample3.txt', 'w') as f:
    f.write('helo this is another test run')

print(f.closed)