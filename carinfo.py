#create
import pickle as p
'''
r=[]
while True:
    mno=int(input('enter model num'))
    cname=input('enter the car name ')
    speed=int(input('enter the car speed'))
    data=[mno,cname,speed]
    r.append(data)
    c=input('if u want to enyer the record (y/n)')
    if c=='n':
        break
a=open('prslcarinfo.dat','ab+')
p.dump(r,a)
print('the record are inserted')
a.close()

# printing1
a=open('D:\\FAISAL\\py\\b data\\my\\prslcarinfo.dat','rb')
x=p.load(a)
for i in x:
    print(i)
x1=p.load(a)
for i in x1:
    print(i)
   
# printing2
a=open('D:\\FAISAL\\py\\b data\\my\\prslcarinfo.dat','rb')
while True:
    s=p.load(a)
    if s:
        print(s)
    else:
        break
# produce error
# serach
a=open('D:\\FAISAL\\py\\b data\\my\\prslcarinfo.dat','rb')
x=p.load(a)
f=0
l=len(a.read())
a.seek(0)
q=0
searchmno=int(input('enter the model no need to search'))
while True:
    if q!=0:
        break
    else:
        while True:
            r=p.load(a)
            for i in r:
                if i[0]==searchmno:
                    print(i,'found')
                    f+=1
                    q+=1
                    break
            if f==1:
                break
              
if f==0:
    print('record not found')
a.close()
'''
#delete
def adlst(r):
    x=p.load(a)
    for i in x:
        r.append(i)
    x1=p.load(a)
    for i in x1:
        r.append(i)
a=open('D:\\FAISAL\\py\\b data\\my\\prslcarinfo.dat','wb+')
r=[]
f=0
adlst(r)
print(r)
qmno=int(input('enter a model num to delete'))
for i in r:
    if i[0]==qmno:
        r.remove(i)
        f+=1
if f==0:
    print('invalid item')
else:
    a.seek(0)
    p.dump(r,a)
    print ('changed')
a.close()

'''
a=open('D:\\FAISAL\\py\\b data\\my\\prslcarinfo.dat','rb')
x=p.load(a)
for i in x:
    print(i)
x1=p.load(a)
for i in x1:
    print(i)
a.close()    

#update
a=open('D:\\FAISAL\\py\\b data\\my\\prslcarinfo.dat','rb+')
s=p.load(fo)
f=0
smno=int(input('enter mno to update speed after servies '))
for r in s:
    if r[0]==smno:
        print('Do you want update',r[1],'speed')
        r[2]=int(input('Enter new speed'))
        f=1
        break
if f==0:
    print('RECORD NOT FOUND')
else:
    fo.seek(0)
    pickle.dump(sd,fo)
    print(' updated')        
fo.close()
  
import pickle
fo=open("xii.dat",'rb')
sd1 = pickle.load(fo)
for a in sd1:
    print(a)
fo.close()
'''













