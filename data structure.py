'''def lsearch(lst,tr):
    j=0
    while j<len(lst) and lst[j]!=tr:
        j+=1
    if j<len(lst):
        return i+1
    else:
        return False'''


def bsearch(lst, tr):
    l = 0
    h = len(lst) - 1
    while l <= h:
        md = int((l + h) / 2)
        if tr == lst[md]:
            return md + 1
        elif tr < lst[md]:
            h = md - 1
        else:
            l = md + 1
    else:
        return False


a = int(input('enter the size of list'))
lst = [0] * a
for i in range(a):
    lst[i] = int(input('element in place of ' + str(i)))
tr = int(input('enter the value to be searched'))
# place = lsearch(lst,tr)
place = bsearch(lst, tr)
if place:
    print('the element', tr, 'is found at', place - 1)
else:
    print('element is not found')
