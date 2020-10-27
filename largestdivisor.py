def find_largest_divisor(n):
    n = n
    largest_divisor = 1
    for x in range(int(n/2)+1,0,-1):
        if(n%x==0):
            largest_divisor = x
            return largest_divisor

def main():
    print(find_largest_divisor(10))

if __name__ == '__main__':
    main()
