def solve(logs):
    from collections import defaultdict
    cache = defaultdict(int)
    most_population = 0
    mpy = None
    for log in logs:
        for yr in range(log[0],log[1]):
            cache[yr] +=1
            if cache[yr] > most_population:
                most_population = cache[yr]
                mpy = yr
            elif cache[yr] == most_population and mpy and mpy > yr:
                mpy = yr
    print(cache)
    return mpy
            
            
# logs = [[1950,1961],[1960,1971],[1970,1981]]
# logs = [[1982,2048],[1968,1973],[2010,2018],[2003,2016],[1952,2003],[1953,1993],[1983,1997],[1976,2032],[1952,1981],[1999,2021]]
logs = [[2008,2026],[2004,2008],[2034,2035],[1999,2050],[2049,2050],[2011,2035],[1966,2033],[2044,2049]]
print(solve(logs))