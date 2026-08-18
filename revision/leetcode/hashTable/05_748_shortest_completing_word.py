def make_dict(a):
    ditt = {}
    a = a.lower()
    for i in a:
        if i.isalpha():
            if i not in ditt:
                ditt[i] = 1
            elif i in ditt:
                ditt[i] +=1
    return(ditt) 


def shortestCompletingWOrd(licensePlate, words):
    actual_plate_dict = make_dict(licensePlate)
    expected_count = len(actual_plate_dict)
    smallest_count = float('inf')
    smallest_count_word = ''
    for i in words:
        count = 0
        new_dict = make_dict(i)
        for j,k in actual_plate_dict.items():
            print(j,k)
            if j not in new_dict or new_dict[j] <k:
                break
            elif j in new_dict and new_dict[j] >= k:
                count +=1
                print(f"this is j {j} and this is k {k}")
        if count >= expected_count:
            if len(i) < smallest_count:
                smallest_count = len(i)
                smallest_count_word = i
            # return i
    return (smallest_count_word, smallest_count)
    



def shortestCompletingWOrd(licensePlate, words):
    ...
    dd






licensePlate = "aBc 12c"
words = ["abccdef","caaacab","cbca"]

# print(make_dict(licensePlate))
print(shortestCompletingWOrd(licensePlate, words))



def hj :
    


