xyz = [i for i in range(50000000)]
print('done')

xyz = (i for i in range(50000000))
print(xyz)

for i in xyz:
    print(i)
