from myparser import *

for fn in ['denominator']: #, 'numerator']:
	n = Parser(fn + '.txt').read()
	n.multout()
	n.sumSameFactors()
	n.suppressImaginary()
	n.sumSameFactors()
	n.pointOut('j')
	for i in range(2):
		for v in ['Ch', 'Sh', 'C', 'S']:#, 'Zr', 'Zi', 'Vr', 'Vi']:
			print i, v
			n.pointOut(v)
	n.writeout(file(fn + '2.txt', 'w'))

	