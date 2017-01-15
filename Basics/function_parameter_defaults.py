def simple(num1, num2):
    pass

def simple(num1, num2=5):
    print(num1, num2)

simple(2)

def basic_window(width, height, font='TNR',
                 bgc='W', scrollbar=True):
    print(width, height, font, bgc)

basic_window(500, 350, bgc='b')
