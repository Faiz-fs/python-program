def fipos(lst, ita):
    s = len(lst)
    if ita < lst[0]:
        return 0
    else:
        p = -1
    for i in range(s - 1):
        if lst[i] <= ita and ita < lst[i + 1]:
            p = i + 1
            break
    if p == -1 and i <= s - 1:
        p = s
    return p


def move(lst, p):
    lst.append(None)
    s = len(lst)
    i = s - 1
    while i > p:
        lst[i] = lst[i - 1]
        i -= 1


lst = [10, 20, 30, 40, 50]
ita = int(input('enter the element to be add'))
pos = fipos(lst, ita)
move(lst, pos)
lst[pos] = ita
print(lst)
