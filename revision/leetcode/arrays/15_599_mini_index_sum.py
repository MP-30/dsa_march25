# list1 = ["happy","sad","good"]
# list2 = ["sad","happy","good"]


# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["KFC","Shogun","Burger King"]


list1 = ["Shogun","Tapioca Express","Burger King","KFC"] 
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]


def findRestaurant(list1, list2):
    common = {}
    for i in range (0,len(list1)):
        if list1[i] in list2:
            common[list1[i]] = [i]
    for j in range(0,len(list2)):
        if list2[j] in common:
            common[list2[j]].append(j)
    minimum_sum = 111111000000
    for i in common.values():
        if sum(i) < minimum_sum:
            minimum_sum = sum(i)
    result = []
    for k,l in common.items():
        if sum(l) == minimum_sum:
            result.append(k)
    return(result)

print(findRestaurant(list1, list2))