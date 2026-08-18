def compute_hcf(x,y):
    while (y):
        x,y = y, x%y
    return x

def compute_lcm(x,y):
    lcm = (x*y)//compute_hcf(x,y)
    return lcm

def main():
    T = int(input())
    
    for _ in range(0,T+1):
        A = int(input())
        B = int(input())
        
        lcm_result = compute_lcm(A,B)
        print(lcm_result)

if __name__ == '__main__':
    main()