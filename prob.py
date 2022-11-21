'''
1) write a func in python to search and display details whos destination is chennai from kpn.dat
assuming the binary containing object in form of records
'''

'''import pickle as p
record=[]
while True:
    pid=int(input("enter passenger id "))
    name=input("enter passenger name")
    age=int(input("enter passenger age"))
    pic=input("enter passenger pickup point")
    desti=input("enter passenger destination point")
    data=[pid,name,age,pic,desti]
    record.append(data)
    choice=input("wish to enter more records(Y/N)?")
    if choice.upper()=='N':
        break
fo=open("kpn.dat","ab")
p.dump(record,fo)
print("record added")
fo.close()

def sdesit():
    a=open('kpn.dat','rb')
    x=int(len(a.read().split())/3)
    for i in range(x):
        data =p.load(a)
        print(data)
        
    a.close()
sdesit()    
print(data)
    d='chennai'
    for i in data:
        if i[len(i)-1]==d:
            print(i)
    a.close()
sdesit()
'''


'''
2) write a progrm in python create a file and cotaining rec
phon no and name a binary data file tele.dat

write the function in python to do following operetion
to append the data
to display the name for given tele num if num doest not eaisit
as rec not found
'''
'''import pickle as p
r=[]
while True:
    name=input("enter name")
    phone_no=int(input("enter phone number"))
    data=[name,phone_no]
    r.append(data)
    choice=input("wish to enter more records(Y/N)?")
    if choice.upper()=='N':
        break
a=open("tele.dat","wb")
p.dump(r,a)
print("record added")
a.close()
def append():
    a=open('tele.dat','ab')
    r=[]
    while True:
        name=input("enter  name")
        phone_no=int(input("enter phone no"))
        data=[name,phone_no]
        r.append(data)
        choice=input("enter more records(Y/N)?")
        if choice.upper()=='N':
            break
    p.dump(r,a)
    a.close()#if seek need to open remove close()
def display():
    a=open('tele.dat','rb')
    n=int(input('enter the num'))
    q=0
    #a.seek(0)
    s1=p.load(a)
    for i in s1:
        if i[-1]==n:
            print('the num owned by:',i[0])
            q+=1
    s2=p.load(a)
    for i in s2:
        if i[-1]==n:
            print('the num owned by:',i[0])
            q+=1
    if q==0:
        print('invalid ')
a=open('tele.dat','ab+')
append()
display()  

import pickle
fo=open("tele.dat",'rb')
sd1 = pickle.load(fo)
for a in sd1:
    print(a)
sd2 = pickle.load(fo)
for a in sd2:
    print(a)
'''



'''
write a progm in python to search detail of those phone which have more than 800 class call.dat
assuming b file contain the following data [phone num,phone call]

a=open('call.dat','wb')
r=[]
while True:
    phone_no=int(input("enter phone no"))
    call=int(input("enter  no of call"))
    data=[phone_no,call]
    r.append(data)
    choice=input("enter more records(Y/N)?")
    if choice.upper()=='N':
        break
p.dump(r,a)
a.close()
def cll():
    a=open('call.dat','rb')
    l=len(a.read())
    a.seek(0)
    for i in range(l):
        if l==a.tell():
            break
        else:
            q=p.load(a)
            for i in q:
                if i[-1]==800:
                    print(i)
            else:
                print('not found')
cll()                
'''


'''
write  a func in python to update a binary file
car model .dat containg the object in the form of
[carmodel no,cc,prize]
the user should enter the model number and updated
prize and display all those updated details

'''
'''
given a binary file xamcenter.dat
contain rec of following
structure [sname,class,sklname,xamcentercode]
write a func tansfer in python that would copy all those rec xcc
as 1100 from master file to
perticularsender.dat
'''

import pickle as p
'''a=open('exam_center.dat','ab')
r=[]
while True:
    sname=input(" enter student name ")
    clas=int(input("enter class"))
    sklname=input('enter skl name ')
    xcode=int(input('enter exam center code'))
    data=[sname,clas,sklname,xcode]
    r.append(data)
    choice=input("enter more records(Y/N)?")
    if choice.upper()=='N':
        break
p.dump(r,a)
a.close()
'''
def cll():
    a=open('exam_center.dat','rb')
    b=open('1100center.dat','wb')
    w=[]
    l=len(a.read())
    a.seek(0)
    for i in range(l):
        if l==a.tell():
            break
        else:
            q=p.load(a)
            for i in q:
                if i[-1]==1100:
                    w.append(i)
    p.dump(w,b)
    a.close()
    b.close()
cll()






























