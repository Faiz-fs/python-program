def eque(q):
    ita=int(input('enter the element to add'))
    q.append(ita)
    if len(q)==1:
        f=r=0
    else:
        r=len(q)-1
def dque(q):
    if q==[]:
        print('queue is underflow')
    else:
        ita=q.pop(0)
    if len(q)==0:
        f=r=None
    print('poped value=',ita)
def peek(q):
    if q==[]:
        print('queue is underflow')
    else:
        f=0
    print('front most value=',q[f])
def display(q):
    if q==[]:
        print('queue is empty')
    elif len(q)==1:
        print(q[0],'-it take both front and rear')
    else:
        f=0
        r=len(q)-1
        print(q[f],'==front value')
        for w in range(1,r):
            print(q[w])
        print(q[r],'==rear')
q=[]
f=None
while True:
    print('queue opp')
    print('1.enqueue')
    print('2.dequeue')
    print('3.peek')
    print('4.display')
    print('5.exit')
    ui=int(input('enter your choice from above'))
    if ui==1:
        eque(q)
    elif ui==2:
        dque(q)
    elif ui==3:
        peek(q)
    elif ui==4:
        display(q)
    elif ui==5 or ui!=5 :
        print('program is terminated')
        break
        























    
