list=[]
newlist=[]
number=int(input('enter the no.of numbers in a list: '))
print('enter the numbers ')
for i in range(number):
	data=int(input())
	list.append(data)
print(list)	
for i in list:
    if i>=0 :
	    newlist.append(i)
print(newlist)
