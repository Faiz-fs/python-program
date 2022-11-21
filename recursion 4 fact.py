def fact(n): #function header #4
    if n<2: 
        return 1  #base case
    return n*fact(n-1)
n=int(input("Enter a number (>0)")) #n=4
result=fact(n) #function calling
print("Factorial of",n,"is",result)

# n=5 5*4*3*2*1


