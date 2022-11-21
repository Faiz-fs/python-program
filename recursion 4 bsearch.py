def bs(ar,se,l,h): #ar=[5,7,12,18,21,25,29,33],se=29,l=6,h=7
    if l>h: #6>7
        return -1  #base case
    m=int((l+h)/2) #m=6+7/2->m=6
    if se==ar[m]: #29==29
        return m  #6 #base case
    elif se<ar[m]: #29 < 25
        h=m-1
        return bs(ar,se,l,h)
    else:
        l=m+1  #l=5+1-->l=6
        return bs(ar,se,l,h)
ar=eval(input("Enter a list"))                 #[5,7,12,18,21,25,29,33,.......,2000]
se=int(input("Enter element to be serached"))  #[0,1, 2, 3, 4, 5, 6, 7,       ,750]
res=bs(ar,se,0,len(ar)-1) #6         #se=29
if res>=0:
    print(se,"found at index",res)
else:
    print("Not FOUND")
        
