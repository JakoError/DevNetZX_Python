import sys

print('{:b}'.format(sum(list(map(lambda x: int(x, 2), sys.argv[1:])))))
