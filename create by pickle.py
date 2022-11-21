
#with pickle
import pickle as p
'''lst=['a','b','c','d','e']
a=open('datafile.txt','wb')
p.dump(lst,a)
a.close()
# without pickle
a=open('myfile.dat','wb+')
l=[100,200,10,5,3,4]
bl=bytearray(l)
a.write(bl)
a.close()
#reading myfile.dat
a=open('D:\FAISAL\\py\\b data\\my\\datafile.txt','rb')
m=p.load(a)
print(m)
#entry of dict data
emailid={1:'faisalfs99945@gmail.com',2:'shreevignesh@gmail.com',3:'thamemkhan2004@gmail.com'}
a=open('emailid.dat','wb')
p.dump(emailid,a)
a.close()
'''
a=open('emailid.dat','rb')
print(p.load(a))
