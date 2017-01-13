exDict = {'Jack':[15, 'blonde'], 'Bob':[22, 'black'], 'Alice':[12, 'brown'], 'Kevin':[17, 'red']}

print(exDict)

print(exDict['Jack'])

exDict['Tim'] = 14

print(exDict)

exDict['Tim'] = 15

print(exDict)




del exDict['Tim']   #remove tim from dictionary

print(exDict)

print(exDict['Bob'])

print(exDict['Jack'][1])
