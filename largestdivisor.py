import sys
import sympy

def find_largest_divisor(n):
    n = n
    largest_divisor = 1
    for x in range(int(n/2)+1,0,-1):
        if(n%x==0):
            largest_divisor = x
            return largest_divisor
        
def find_largest_div_better(n):
    if(n==1):
        return 1
    return find_largest_div_recursive(int(n),2)        

def find_largest_div_recursive(n,x):
    if(n%x==0):
        return int((n/x))
    else:
        return find_largest_div_recursive(n,sympy.nextprime(x))

def main(n):
  print(find_largest_div_better(int(n)))

if __name__ == "__main__":
    if(len(sys.argv)==2):
        main(sys.argv[1])
    else:
        print("One and only one command line argument, please!")
   
