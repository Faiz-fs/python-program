#1
'''
def  f():
    a=open('try.txt','r')
    c=input('enter the search element')
    l=a.read().lower().split()
    print(l.count(c))
    #q=0
    #for i in l:
        #if i.lower()==c:
            #q+=1
    #print(q)
    a.close()
f()    
#2
def wr():
    a=open('myfile.txt','w')
    while True:
        q=input('enter char')
        if q=='#':
            print('content added')
            break
        else:
            a.write(q)
    a.close()
wr()
'''
'''Assume that a text file named text1.txt already contains some
text written into it, write a function named vowelwords(), that
reads the file text1.txt and create a new file named text2.txt,
which shall contain only those words from the file text1.txt
which don’t start with an uppercase vowel(i.e., with
‘A’,’E’,’I’,’O’,’U’).
for example if the file text1.txt contains:
Take One Apple And one glass milk daily.
Then the file text2.txt shall contain :
Take one glass milk daily

def vowelwords():
    a=open('text1.txt','r')
    b=open('text2.txt','w')
    x=['A','E','I','O','U']
    l=a.read().split()
    for i in l:
        if i[0] not in x:
            b.write(i+' ')
    b.write('.')        
    a.close()
    b.close()
vowelwords()    
'''
'''
Write a function in python to calculate the average word size
in a text file “Report.txt”, each word is separated by single
space or full stop
'''
a=open('text1.txt','r')
l=a.read().split()
#x=l.count('.')
f=q=0
for i in l:
    if '.' in i:
        y=i.split('.')
        for j in y:
            f+=1
            q+=len(j)
    else:
        f+=1
        q+=len(i)
print((q)/f)    
a.close()        
        
    





'''7. Write a function in python to count the number of words
present in the text file “MyFile.txt”. Assume that each word is
separated by a blank space and no blank space appears in the
beginning and at the end of the file.
8. Write a function in python to count the words “this” and
“these” present in a text file “ARTICLE.TXT”.
[Note that the words “this” and “these” are complete words]
9. Write a function in python to print the count of the word which
is as an independent and most occurrence word in at text file
DIALOGUE.TXT.
10. Write a function in python to count the number of lines
starting with a digit in a text file “Diary.Txt”.'''















