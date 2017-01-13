exec("print('so this works like eval')")

list_str = "[4,5,6,7,2]"
list_str = exec(list_str)
print(list_str)

exec("list_str2 = [4,5,6,2,5]")
print(list_str2)

exec("def test(): print('lalalalalala bamba')")
test()

exec("""
def test2():
    print('lets see if multi line works.....')
""")

test2()
