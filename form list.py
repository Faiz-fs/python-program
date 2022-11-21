#list expression
#1)variable=[expression for loop]
#2)variable=[expression for loop condition]
#3)variable
#for loop:
#     condition:
#          expression
#4)varilable=[expression condition for loop]
'''l6=[n*2 for n in range (1,11)]
l6=[]
for i in range (1,11):
    l6.append(i*2)
print(l6)    
values=[31,15,42,12,5,39,21,61,25]
x=[y for y in values if y%3==0]
print(x)'''
lst=[('a',11),('b',12),('c',13)]
lst1=[n*3 for (x,n) in lst if x=='b'or x=='c']
print(lst1)

