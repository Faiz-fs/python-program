'''def reverse(s):
    if len(s)==0:
        return
    t=s[0]
    reverse(s[1:])
    print(t,end='')
s=input('enter the str')
reverse(s)

def pala(s):
    l=0
    h=len(s)
    if s[l]==s[h-1]:
        k=True
        pala(s[1:(h-2)])
        if k:
            print('yes')
        else:
            print('not')
    else:
        print('not')
s='malayalam'
pala(s)
'''
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
a=int(input('enter the value1'))
b=int(input('enter the value2'))
if a>b:
    print(gcd(a,b))
else:
    print(gcd(b,a))
            
