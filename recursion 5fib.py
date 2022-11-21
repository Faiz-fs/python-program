def fib(n): #1,2,3,4,5
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)#fib(4)+fib(3)  n=5->2+1
n=int(input("enter last term")) #__main__  n=5
for i in range(1,n+1): #[1,2,3,4,5]
    print(fib(i),end=",") #1,2,3,4,5
print(".........")

#0,1,1,2,3,5,8,...........n
#0,1,1,2,3,.........












'''
def fib(i):
    if(i<= 1):
        return i
    else:
        return(fib(i-1) + fib(i-2))
length = int(input("Enter number of terms:"))
print("Fibonacci sequence using Recursion :")
for iter in range(length):
    print(fib(iter))
'''
