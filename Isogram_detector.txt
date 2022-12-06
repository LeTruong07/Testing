mystr = (input('Enter a word :')).lower()
mylist = 'q w e r t y u i o p a s d f g h j k l z x c v b n m'.split(' ')
checkiso = []
T1 = False
T2 = False
for i in mystr:
    if i not in checkiso:
        checkiso.append(i)
        T1 = True
    else:
        T2 = True
if T1 == True and T2 == True:
    print("Not Isogram")
else:
    print("Isogram")
