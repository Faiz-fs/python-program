def traverse(lst):
    s=len(lst)
    for i in range (s):
        print(lst[i],end=' ')
a=int(input('enter size of lst'))
lst=[0]*a
for i in range(a):
    lst[i]=int(input('element'+str(i)+':'))
print(lst,'after traversing is ')
traverse(lst)
        
        
