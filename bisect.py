import bisect
lst=[100,90,80,70,60,40]
lst.reverse()
ita=int(input('enter the element to inserted'))
i=bisect.bisect(lst,ita)
bisect.insort(lst,ita)
lst.reverse()
print('the list after inserted is',lst)
