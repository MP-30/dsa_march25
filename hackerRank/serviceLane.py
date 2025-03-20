n = 5
width = [1,2,2,2,1]
cases = [[2, 3], [1, 4], [2, 4], [2, 4], [2, 3]]


def serviceLane(n, cases):
    min_index = 0
    max_index = 0
    result = []
    for i in cases:
        min_index = i[0]
        max_index = i[1]
        min_value = min(width[min_index:max_index+1])
        # print(f'width is  {width[min_index:max_index+1]}')
        # print(f"min {min_index} max {max_index}")
        result.append(min_value)
        # print(f'min value for {min_index}, {max_index} is {min_value}')
    return (result)

print(serviceLane(n, cases))


    # 2

    # 1

    # 1

    # 1

    # 2