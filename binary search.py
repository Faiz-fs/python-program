def binsearch(ar,se): #se=21 ar=#[10,12,14,21,23,28,31,37,42,44,49,53]
    low=0  #0,
    high=len(ar)-1 #11
    while low <= high:   #3<=4
        mid=int((low+high)/2) #(3+4)/2->3  mid=3
        if se == ar[mid]: #21==21
            return mid #3
        elif se < ar[mid]: #21<14
            high=mid-1  #high=5-1=4
        else:
            low=mid+1 #low=2+1
    else:      #loop's else
        return -1        #[10,12,14,21,23,28,31,37,42,44,49,53]
list1=eval(input("Enter a list in ascending order"))
se=int(input("Enter searching element")) #21
result=binsearch(list1,se) #3
if result >= 0: #if result holds 0....n-1 value
    print(se,"FOUND at index",result)
else:
    print("Sorry..!",se,"NOT FOUND in the list")
    
    
