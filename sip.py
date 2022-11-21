def revto():
    a=open('D:\\FAISAL\\py\\txt\\tu.txt','a+')
    l=a.read().split()
    for i in l:
        if i.lower()=='to':
            i=i[::-1]
    a.writelines(l)        
    a.close()
revto()    
