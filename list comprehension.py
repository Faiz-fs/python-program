'''
l=[]
for i in range(1,6):
    l.append(i*2)
print(l)
#l=[2,4,6,8,10]
'''
'''
L=[i*2 for i in range(1,6)] #: no need
print(L)
'''
#variable=[expression to create list for(set values to iterate)if condition]
#variable=[expression to create list if condition else condition for(set values to iterate)]
# or
#for(set values to iterate):
#    condition    
#    expression to create list
'''
l=[I*2 for I in range(1,8,2)] #[1,3,5,7]
print(l)
#[2,6,10,14]
'''
'''
l=[]
for i in range(1,50):
    if i%7==0:
        l.append(i*2)
print(l)
#[14,28,42,56,70,84,98]
'''
'''
a=[i*2 for i in range(1,50) if i%7==0]
print(a)
'''
'''
l=[n for n in range(1,50) if n%7==0]
print(l)
'''
'''
#[2,3,4,5,6,7,8]
l=[n if n<5 else n*2 for n in range(2,9)]
print(l)
'''
'''
l=[n if n<5 else n*2 for n in range(2,9)]
print(l)
'''
#l=[2,4,6,8,10,12,14,16,18,20]
#l=[n*2 for n in range(1,11)]
'''
l=[]
for n in range(1,11):
    l.append(n*2)
print(l)

values=[31,15,42,12,5,39,21,61,25]
x=[y for y in values if y%3==0]
print(x)
#[15,42,12,39,21]


lst=[('a',11),('b',12),('c',13)] #('a',11)
nlst=[n*3 for(x,n)in lst if x=='b' and n==12]#x=c,n=13
print(nlst)
#[36,39]
#variable=[expression to create list for(set values to iterate)if condition]
#[33,36]


r=['E' if i%2==0 else 'O' for i in range(10,20)]#[10,11,....,19]
print(r)
#variable=[expression to create list for(set values to iterate)if condition]
#variable=[expression to create list if condition else statement for(set values to iterate)]
#['E','O','E','O','E','O','E','O','E','O']

r=[]
for x in [10,5,2]:
    for y in [2,3,4]:
        r.append(x**y)
print(r)
#[100,1000,10000,25,125,625,4,8,16]
'''
'''
r=[x**y for x in [10,5,2] for y in [2,3,4]]
print(r)
'''                                                             
r=[(x,y) for x in range(5) if x%2==0 for y in range(5) if y%2==1]
print(r)
#[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]









