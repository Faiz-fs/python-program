def bsearch(lst, item):
    l = 0
    h = len(lst) - 1
    while l <= h:
        md = int((l + h) / 2)
        if item == lst[md]:
            return md + 1
        elif item < lst[md]:
            h = md + 1
        else:
            l = md + 1
    else:
        return False


lst = [1, 2, 3, 4, 5, 6, 7, 8]
item = int(input('enter the element need to be deleted'))
pos = bsearch(lst, item)
if pos:
    del lst[pos - 1]
    print('the list after deleting of ', item, 'is', lst)
else:
    print('element not found')
