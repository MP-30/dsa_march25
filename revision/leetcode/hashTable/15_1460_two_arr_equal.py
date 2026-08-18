def canBeEqual(target, arr):
    
    def make_dict(a):
        res = {}
        for i in a:
            if i not in res:
                res[i] = 1
            elif i in res:
                res[i] +=1
        return res
    if target == arr:
        return True
    elif make_dict(target) == make_dict(arr):
        return True
    else: return False
    
# target = [1,2,3,4]
# arr = [2,4,1,3]
# target = [7]
# arr = [7]
target = [3,7,9]
arr = [3,7,11]
print(canBeEqual(target, arr))