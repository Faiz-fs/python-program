def strrev(s,n):
    if n>0:
        print(s[n],end='')
        strrev(s,n-1)
    elif n==0:
        print(s[0])
s=input('enter the str')
strrev(s,len(s)-1)
