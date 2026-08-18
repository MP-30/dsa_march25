cards = [13,11,10,7,4,3,1]
query = 7
output = 3
tests = []
test = {
    "input": {
        'cards' : [13,11,10,7,4,3,1],
        'query' : 7
    },
    'output' : 3
}
tests.append(test)

tests.append({
    "input": {
        'cards' : [13,11,10,7,4,3,1,0],
        'query' : 1
    },
    'output' : 6
})
tests.append({
    "input": {
        'cards' : [4,2,1,-1],
        'query' : 4
    },
    'output' : 0
})
tests.append({
    "input": {
        'cards' : [3,-1,-9,-127],
        'query' : -127
    },
    'output' : 3
})
tests.append({
    "input": {
        'cards' : [6],
        'query' : 6
    },
    'output' : 0
})

tests.append({
    "input": {
        'cards' : [9,7,5,2,-9],
        'query' : 4
    },
    'output' : -1
})

tests.append({
    "input": {
        'cards' : [],
        'query' : 4
    },
    'output' : -1
})

tests.append({
    "input": {
        'cards' : [8, 8, 6, 6, 6, 6, 6, 6, 3,2,2,2,0,0,0],
        'query' : 3
    },
    'output' : 7
})

tests.append({
    "input": {
        'cards' : [8, 8, 6, 6, 6, 6, 6, 6, 3,2,2,2,0,0,0],
        'query' : 6
    },
    'output' : 2
})
print(tests)
def locate_card1(cards, query):
    position = 0
    if len(cards) >0:
        while True:
            if cards[position] == query:
                return position
            position +=1
            if position == len(cards):
                return -1
    else: return -1    

def locate_card2(cards, query):
    ...
    lo, hi = 0, len(cards)-1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        
        # print("lo:", lo, "hi:", hi, "mid:", mid, "Mid_number:", mid_number)
        
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid -1
        elif mid_number > query:
            lo = mid + 1
    return -1    

def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid -1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards)-1
    
    while lo <=hi:
        mid = (lo + hi) //2
        result = test_location(cards, query, mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = min -1
        elif result == 'right':
            lo = mid +1
    return -1


# final technic

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        else: 
            lo = mid +1
    return -1

def locate_card0(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid -1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else: 
            return 'right'
    return binary_search(0, len(cards) - 1, condition)


print("Running tests for locate_card function:")
for i, test in enumerate(tests):
    cards_input = test['input']['cards']
    query_input = test['input']['query']
    expected_output = test['output']

    actual_output = locate_card1(cards_input, query_input)
    
    # Check if actual output matches expected output
    is_correct = (actual_output == expected_output)
    
    print(f"Test {i+1}:")
    print(f"  Input: cards={cards_input}, query={query_input}")
    print(f"  Expected: {expected_output}, Actual: {actual_output}")
    print(f"  Result: {'PASS' if is_correct else 'FAIL'}")
    if not is_correct:
        print(f"  --- FAILED: Expected {expected_output}, got {actual_output} ---")
    print("-" * 30)

'''
time complexity

first iteration = n

second iteration = n/2

third iteration = n/4 or n/2^2

iteration k = n/2^k

since final length of array is 1 we can find the

n/2^k = 1

rearranging the term 

n = 2^k

taking the logarithm

k = log n

so overall complexity is O(log N)
which is 50,000 times faster then n

'''