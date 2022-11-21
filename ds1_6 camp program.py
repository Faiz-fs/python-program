def addloc(cmp):#cmp='12pollachi','15udmp','18cbe','14erode'
    dd=cmp[0:2] #[12,15,18,14]
    ln=len(planned)#3
    if ln==0: #3==0
        planned.append(cmp)#planned=['12pollachi',]
    else:
        last=planned[ln-1] #last='18cbe'
        if int(dd)>= int(last[0:2]): #14>=18
            planned.append(cmp) #planned=['12pollachi','14erode','15udmp','18cbe']
        else:
            for i in range(ln): #[0,1,2] i=1
                cp=planned[i] #cp='15udmp'
                if int(dd)<= int(cp[0:2]): #14<=15
                    planned.insert(i,cmp)#planned=['14erode','15udmp','18cbe']
                    break
def conductcamp(cmp,p): #'12pollachi',1000
    global ppl
    ppl+=p #1000
    conducted.append(cmp) #conducted=['12pollachi']
    planned.remove(cmp) 
def search(cmp,lst):#cmp=cbe lst=['14erode','15udmp','18cbe']
    ln=len(lst) #ln=3
    for i in range(ln): #[0,1,2]
        if cmp in lst[i]: #cmp=salem
            return lst[i] #'18cbe'
    else:
        return False
def report():
    lenp=len(planned) #lenp=3
    lenc=len(conducted)#lenc=1
    print("\t REPORT")
    print("________________")
    print("Camps conducted so far=",lenc)
    print("People served so far=",ppl)
    print("Camps to be conducted=",lenp)
    print("________________")
def display():
    print("Camps Planned:", end=' ')
    for i in planned:
        print(i,end=',')
    print("...!")
    print("Camps conducted so far:",end=' ')
    for i in conducted:
        print(i,end=' ')
    print("...!")
planned=[] #
conducted=[] #
ppl=0 #
ch=0  #
while ch!=6: #4!=6 ch=3
    print("\t---")
    print("\tMENU")
    print("\t---")
    print("1.Add camp Location")
    print("2.Camp Conducted")
    print("3.Look for a camp")
    print("4.Report")
    print("5.Display List")
    print("6.Exit")
    ch=int(input("Enter your choice(1-6):")) #ch=5
    if ch==1: #2==1
        cm=input("Enter camp location") #erode
        dd=input("Enter date of the month(only dd):")#14
        cmp=dd+cm #'12pollachi','15udmp','18cbe','14erode'
        addloc(cmp)#'12pollachi','15udmp','18cbe','14erode'
    elif ch==2:#2==2
        cm=input("Camp conducted at location?")#salem
        p=int(input("How many people are served at this camp"))#2000
        result=search(cm,planned)#result='False'
        if result==False:
            print("Sorry no camp in the list")
        else:
            conductcamp(result,p)#
    elif ch==3: #3==3
        cm=input("Enter camp location") #cbe
        r1=search(cm,planned) #'18cbe'
        if r1==False:
            r2=search(cm,conducted) #RESULT 2
            if r2==False:
                print("Sorry no such camp in our list")
            else:
                dd=r2[0:2]
                print(cm,"was conducted on date",dd,"of this month")
        else:
            dd=r1[0:2]#dd=18
            print(cm,"camp is to be conducted on date",dd,"of this month")
    elif ch==4:#4==4
        report()
    elif ch==5:#5==5
        display()
    elif ch!=6:
        print("Wrong choice, Enter choice from 1 to 6 only")
    else:
        print("Thank you")
