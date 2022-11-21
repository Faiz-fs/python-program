#binary search
'''def search(aw,lst):
    l=0
    h=len(lst)-1
    while l<=h:
        md=int((l+h)/2)
        if aw==lst[md]:
            return md
        elif aw<lst[md]:
            h=md-1
        else:
            l=md+1
    else:
        return -1
lst=eval(input('enter the list'))
lst.sort()
aw=int(input('enter the value u need to find'))
r=search(aw,lst)
if r >=0:
    print(aw,'is found at index of ',r+1)
else:
    print('element is not found')
'''
#recursion for binary search
'''def bs(lst,a,l,h):
    if l>h:
        return -1
    md=int((l+h)/2)
    if a==lst[md]:
        return md
    elif a<lst[md]:
        h=md-1
        return bs(lst,a,l,h)
    else:
        l=md+1
        return bs(lst,a,l,h)
lst=eval(input('enter the list'))
lst.sort()
a=int(input('enter the element to be find'))
r=bs(lst,a,0,len(lst)-1)
if r>=0:
    print('the element is found at index',r,'at the list',lst)
else:
    print('not found')
'''

# recursion of factorial
'''def fact(a):
    if a<2:
        return 1
    return a*fact(a-1)
a=int(input('enter a num'))
r=fact(a)
print('factorial value of ',a,' is ',r)
'''

# recursion of fibanoci
'''def fib(a):
    if a==1:
        return 0
    elif a==2:
        return 1
    else:
        return fib(a-1)+fib(a-2)
q=int(input('enter the num'))
for i in range (1,q+1):
    print(fib(i),end=',')
'''    
















































