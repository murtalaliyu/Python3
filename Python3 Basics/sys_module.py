import sys
'''
sys.stderr.write('This is stderr text\n')
sys.stderr.flush()

sys.stdout.write('This is stdout text\n')

print(sys.argv)


if len(sys.argv) > 1:
    print(float(sys.argv[1]) + 5)
'''
def main(arg):
    print(arg)

main(sys.argv[1])
