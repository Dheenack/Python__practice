def hw():
    print("Hello world")

## Sum of two numbers
def sum_of_2_numbers(a:int,b:int)->int:
    return a+b

## Even or odd
def evenOrOdd(num:int)->None:
    print("EOvdedn"[num%2::2])

def fact(n:int)->int:
    if(n<0): return -1
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

def fibo(n:int)->None:
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,b+a

def isPalindrome(string:str)->bool:
    i,j=0,len(string)-1
    flag=True
    while(i<j):
        if(string[i]!=string[j]):
            flag=False
        i+=1;j-=1
        if(flag): return True
        return False

def reverse_string(string:str)->str:
    j=len(string)-1
    s=""
    while(j>=0):
        s+=string[j]
        j-=1
    return s


if __name__=="__main__":
    # evenOrOdd(5)
    # hw()
    # print(fact(0))
    # fibo(5)
    print(reverse_string("hello"))
    print(isPalindrome("12321"))