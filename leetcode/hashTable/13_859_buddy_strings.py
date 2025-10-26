# def buddyStrings(s, goal):
#     ...
#     unmatched = {}
#     if len(s) != len(goal):
#         print(1)
#         return False
#     elif len(set(s)) == 1 and  len(set(goal)) ==1:
#         print(2)
#         return True
#     else:
#         for i in range(len(s)):
#             if s[i] != goal[i]:
#                 if s[i] not in unmatched:
#                     unmatched[s[i]] = [i]
#                 elif s[i] in unmatched: 
#                     unmatched[s[i]].append(i)
#                 if goal[i] not in unmatched:
#                     unmatched[goal[i]] = [i]
#                 elif goal[i] in unmatched: 
#                     unmatched[goal[i]].append(i)
#     print(unmatched)
#     if len(unmatched) ==2:
#         sorted_value = 0
#         for j in unmatched.values():
#             if sorted_value ==0:
#                 sorted_value = sorted(j)
#             elif sorted_value != 0:
#                 if sorted(j) == sorted_value:
#                     print(3)
#                     return True
#     print(4)
#     return False
    
def buddyStrings(s, goal):
    ...
    if len(s) != len(goal):
        return False
    
    if s == goal:
        return len(set(s)) < len(s)
        
    new_s , new_goal = [] ,[]
    
    for i in range(len(s)):
        if s[i] != goal[i]:
            new_s.append(s[i])
            new_goal.append(goal[i])
            
    return len(new_s) == 2 and new_s[::-1] == new_goal
    

# s = 'abab'
# goal = 'abab'    

# s = "abcaa"
# goal = "abcbb"


# s = 'abcd'
# goal = 'cbad'

# s = 'ab'
# goal = 'ba'

s = 'ab'
goal = 'ab'

# s = 'aa'
# goal = 'aa'

print(buddyStrings(s,goal))

# print(set(s))