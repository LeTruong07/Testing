mylist = []
for i in range(8):
  mountain_h = int(input())
  mylist.append(mountain_h)
while not max(mylist) == 0 :
 print(mylist.index(max(mylist)))
 mylist[mylist.index(max(mylist))] = 0
