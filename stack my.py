def empty(s):
    if s==[]:
        return True
def push(s,ita):
    s.append(ita)
    top=len(s)-1
def pop(s):
    if empty(s):
        return 'underflow'
    else:
        ita=s.pop()
        if len(s)==0:
            top=None
        else:
            top=len(s)-1
        return ita
def peek(s):
    if empty(s):
        return 'underflow'
    else:
        top=len(s)-1
        return s[top]
def display(s):
    if empty(s):
        print('stack is empty')
    else:
        top=len(s)-1
        print(s[top],'<-top')
        for i in range (top-1,-1,-1):
            print(s[i])
s=[]
top=None
while True:
    print('1.push')
    print('2.pop')
    print('3.peek')
    print('4.display stack')
    print('5.exit')
    c=int(input('enter the choice 1-5'))
    if c==1:
        ita=int(input('enter the item to insert'))
        push(s,ita)
    elif c==2:
        ita=pop(s)
        if ita=='underflow':
            print('stack is empty')
        else:
            print('poped item is ',ita)
    elif c==3:
        ita=peek(s)
        if ita=='underflow':
            print('stack is empty')
        else:
            print('peeked element',ita)
    elif c==4:
        display(s)
    elif c==5:
        print('stack is over')
        break
    
