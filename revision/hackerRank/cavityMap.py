grid = ['1112', '1912', '1892', '1234']

def cavityMap(grid):
    grid_list = [list(row) for row in grid] 
    # print(grid_list)
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if (i != 0 and j !=0 and i != len(grid)-1 and j != len(grid)-1) : 
                if grid[i-1][j] < grid[i][j] and grid[i][j-1] < grid[i][j] and grid[i+1][j] < grid[i][j] and grid[i][j+1] < grid[i][j]:
                        grid_list[i][j] = 'X'

    grid = ["".join(row) for row in grid_list]
    return(grid)

print(cavityMap(grid))

# def cavityMap(grid):
#     # Convert list of strings to list of lists (manual method)
#     grid_list = []
#     for row in grid:
#         print(list(row))
#         grid_list.append(list(row))


# cavityMap(grid)
