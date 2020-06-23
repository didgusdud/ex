import sys

f1 = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'w')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
