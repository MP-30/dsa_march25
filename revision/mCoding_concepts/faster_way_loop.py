# def hello():
#     with open(...) as fp:
#         ...
        
#     fp = open(...)
    
#     try:
#         ...
#     finally:
#         fp.close()
        
def cm_examples():
    with open ("test.txt", "w") as fp:
        fp.write("hello world")
        