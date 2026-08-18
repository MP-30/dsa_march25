def dd(arr):
    from collections import Counter
    ddr = Counter(arr)
    if len(ddr.values()) == len(set(ddr.values())):
        return True
    else: return False
    ...
    
    
arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(dd(arr))