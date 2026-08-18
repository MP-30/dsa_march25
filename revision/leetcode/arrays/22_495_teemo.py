def time_series_ques(timeSeries, duration):
    start_len = 0
    for i in range(0,len(timeSeries)-1):        
        time = min(duration, (timeSeries[i+1] - timeSeries[i]))
        print(time)
        start_len += time

    print(start_len + duration)
    
t = [1,4]
d = 2
time_series_ques(t,d)