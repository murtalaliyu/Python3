names = ['Jeff', 'Gary', 'Jill', 'Samantha']

'''
for name in names:
    #print('Hello there, ' + name)
    print(' '.join(['Hello there', name]))
'''

'''
print(', '.join(names))

import os

location_of_files = '/Users/Murtala/Desktop/Python3/Intermediate'
file_name = 'string_concatenation&formatting.py'

print(location_of_files + '/' + file_name)

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())
'''

who = 'Gary'
how_many = 12

print(who, 'bought', how_many, 'apples')
print('{} bought {} apples today!'.format(who, how_many))
print('{1} bought {0} apples today!'.format(who, how_many))
