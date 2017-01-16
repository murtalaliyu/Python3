input_list = [3,5,2,10,15,20,5,2,1,3,100]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))

'''
xyz = []
for i in input_list:
    if div_by_five(i):
        xyz.append()
'''

#[print(i) for i in xyz]

xyz = [i for i in input_list if div_by_five(i)]
#print(xyz)
#[print(i) for i in xyz]
#(print(i) for i in xyz)

[print(i, ii) for ii in range(5) for i in range(5)]



