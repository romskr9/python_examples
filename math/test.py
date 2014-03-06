from mymath import *

f = file ('aaa')
# c = f.read(1)
# while not c == '':
	# print 123, c
	# c = f.read(1)

parser = Parser('aaa')

tree = parser.read()

print tree

#tree.debug(file('ddd', 'w'))
tree.debug()

tree.writeout(file('bbb', 'w'))