l=[]
r=int(input("How many rows"))
c=int(input("How many cols"))
for i in range(r):
    row=[] 
    for j in range(c):
        e=int(input("Element"+str(i)+","+str(j)+":")) 
        row.append(e) 
    l.append(row) 
print(l)

