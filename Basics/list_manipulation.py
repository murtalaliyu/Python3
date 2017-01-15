x = [4,3,5,6,6,5,6,5,4,6,4,5,6,4,5]

x.append(2)     #adds 2 to the end of the list

x.insert(2, 99) #instert 99 into the 2th element

x.remove(2)     #removes all 2s

x.remove(x[1])  #removes the 1th element

print(x)
print(x[5:7])
print(x[-1])    #prints last element in list
print(x[-2])    #prints 2nd to last element in list
print(x.index(99))
print(x.count(6))

x.sort()
print(x)

y = ['Janet', 'Jessy', 'Kelly', 'Alice', 'Joe', 'Bob']

y.sort()
print(y)
