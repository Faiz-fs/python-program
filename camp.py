def adloc(c):
    d=c[0:2]
    l=len(plan)
    if l==0: 
        plan.append(c)
    else:
        lst=plan[l-1] 
        if int(d)>= int(lst[0:2]): 
            plan.append(c) 
        else:
            for i in range(l): 
                cp=plan[i] 
                if int(d)<= int(cp[0:2]): 
                    plan.insert(i,c)
                    break
def cdtcmp(c,p): 
    global pl
    pl+=p 
    cdt.append(c) 
    plan.remove(c) 
def search(c,lt):
    l=len(lt) 
    for i in range(l): 
        if c in lt[i]: 
            return lt[i] 
    else:
        return False
def report():
    lp=len(plan) 
    lc=len(cdt)
    print("camps conducted so far=",lc)
    print("people served so far=",pl)
    print("camps to be conducted=",lp)
def display():
    print("camps planned:", end=' ')
    for i in plan:
        print(i,end=',')
    print("camps conducted so far:",end=' ')
    for i in cdt:
        print(i,end=' ')
    print()    
plan=[] 
cdt=[] 
pl=0 
ui=0  
while ui!=6: 
    print('1.add camp Location')
    print('2.camp Conducted')
    print('3.look for a camp')
    print('4.report')
    print('5.display List')
    print('6.exit')
    ui=int(input("enter your choice(1-6):")) 
    if ui==1: 
        loc=input('enter camp location') 
        d=input('enter date of this month')
        c=d+loc 
        adloc(c)
    elif ui==2:
        loc=input('eamp conducted at location')
        p=int(input('no of people served in the camp'))
        result=search(loc,plan)
        if result==False:
            print('sorry no camp in the list')
        else:
            cdtcmp(result,p)
    elif ui==3: 
        loc=input('enter camp location') 
        r1=search(c,plan) 
        if r1==False:
            r2=search(c,cdt) 
            if r2==False:
                print('sorry no camp is in list')
            else:
                d=r2[0:2]
                print(c,'was conducted on ',d,'of this month')
        else:
            d=r1[0:2]
            print(c,'is to be conducted on ',d,'of this month')
    elif ui==4:
        report()
    elif ui==5:
        display()
    elif ui!=6:
        print('wrong choice, enter choice from 1 to 6 only')
    else:
        print('thank you')

    
