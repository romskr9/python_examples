from unittest import *
from glob import *
from os import *

from myparser import *

class TestMath(TestCase):
	
	def assertFileEqual(self, file1, file2):
		s1 = file(file1).read()
		s2 = file(file2).read()
		self.assertEqual(s1, s2, '\nsrc1:%s\nsrc2:%s' % (s1, s2))
	
	def setUp(self):
		for path in glob('tests\\*.tst'):
			remove(path)
	
	def tearDown(self):
		self.setUp()
		
	def loadFromString(self, str):
		f = file('tests\\tempfile.tst', 'w').write(str)
		n = Parser('tests\\tempfile.tst').read()
		return n
		
	def test_1(self):
		nTests = 2	
		for i in range(0, nTests):
			print 'test pass', i
			Parser('tests\\%i.in' % i).read().writeout(file('tests\\%i.tst' % i, 'w'))
			self.assertFileEqual('tests\\%i.tst' % i, 'tests\\%i.out' % i)
			
	def test_multiplewith(self):
		n = Parser('tests\\tmw.in').read()
		for i in range(n.len()):
			n.data[i].multiplewith(-2)
		n.writeout(file('tests\\tmw1.tst', 'w'))
		n.multiplewith(-2)
		n.writeout(file('tests\\tmw2.tst', 'w'))
		self.assertFileEqual('tests\\tmw1.tst', 'tests\\tmw1.out')
		self.assertFileEqual('tests\\tmw2.tst', 'tests\\tmw2.out')
		
	def test_normalize(self):
		nTests = 4
		sizes = {3: 4}
		for i in range(0, nTests):
			print 'test pass', i
			n = Parser('tests\\norm%i.in' %i).read()
			n.normalize()
			n.writeout(file('tests\\norm%i.tst' %i, 'w'))
			if i in sizes:
				self.assertEqual(n.size(), sizes[i])
			self.assertFileEqual('tests\\norm%i.tst' % i, 'tests\\norm%i.out' % i)

	def test_normalize_alwaysNum(self):
		nTests = 4
		nodea = ['a',  '11',  'a+2b', 'ab-1', 'ab+1', '1a(b+2)']
		nodeb = ['a',  '11',  '1a+2b', '1ab-1', '1ab+1', '1a(b+2)']
		for i in range(0, nTests):
			print 'test pass', i
			na = self.loadFromString(nodea[i])
			nb = self.loadFromString(nodeb[i])
			na.normalize(alwaysNum = True)
			nb.normalize()
			self.assertEqual(Node.compare(na, nb), True)

	def test_multout(self):
		nTests = 3
		for i in range(0, nTests):
			print 'test pass', i
			n = Parser('tests\\multout%i.in' %i).read()
			n.multout()
			n.writeout(file('tests\\multout%i.tst' %i, 'w'))
			self.assertFileEqual('tests\\multout%i.tst' % i, 'tests\\multout%i.out' % i)
			
	def test_size(self):
		nTests = 2
		sizes = [8, 8]
		for i in range(0, nTests):
			print 'test pass', i
			n = Parser('tests\\%i.in' % i).read()
			self.assertEqual(n.size(), sizes[i])
	
	def test_compare(self):
		nTests = 6
		nodea = ['a',  '11',  'a+b', 'ab-1', '-ab+1', 'a(b+2)']
		nodeb = ['a',  '11',  'a+b', '-1+ab', '1-ab', '(2+b)a']
		for i in range(0, nTests):
			print 'test pass', i
			file('tests\\cmpa%i.tst' % i, 'w').write(nodea[i])
			na = Parser('tests\\cmpa%i.tst' % i).read()
			file('tests\\cmpb%i.tst' % i, 'w').write(nodeb[i])
			nb = Parser('tests\\cmpb%i.tst' % i).read()
			self.assertEqual(Node.compare(na, nb), True)
			file('tests\\cmpbb%i.tst' %(nTests - i - 1), 'w').write(nodeb[nTests - i - 1])
			nb = Parser('tests\\cmpbb%i.tst' % (nTests - i - 1)).read()
			self.assertEqual(Node.compare(na, nb), False)
		
	def test_compare_no_respect_to_number(self):
		nTests = 6
		nodea = ['1a',  '11',  'a+b', 'ab-1', 'ab+1', '1a(b+2)']
		nodeb = ['2a',  '11',  'a+b', '-1+3ab', '1-ab', '2(2+b)a']
		for i in range(0, nTests):
			print 'test pass', i
			file('tests\\cmpa%i.tst' % i, 'w').write(nodea[i])
			na = Parser('tests\\cmpa%i.tst' % i).read()
			file('tests\\cmpb%i.tst' % i, 'w').write(nodeb[i])
			nb = Parser('tests\\cmpb%i.tst' % i).read()
			self.assertEqual(Node.compare(na, nb, respect = False), True)
			file('tests\\cmpbb%i.tst' %(nTests - i - 1), 'w').write(nodeb[nTests - i - 1])
			nb = Parser('tests\\cmpbb%i.tst' % (nTests - i - 1)).read()
			self.assertEqual(Node.compare(na, nb, respect = False), False)

	def test_sum_the_same_factors(self):
		nTests = 6
		nodea = ['1a+a3',  '11-1',  'b-a+1b-b2', 'ab-(ba)', 'a(c+1)+1(1+c)a', '1a(b+2)-2(b+2)a']
		nodeb = ['4a',  '10',  '-a', '0', '2a(1+c)', '-1a(2+b)']
		for i in range(0, nTests):
			print 'test pass', i
			file('tests\\cmpa%i.tst' % i, 'w').write(nodea[i])
			na = Parser('tests\\cmpa%i.tst' % i).read()
			file('tests\\cmpb%i.tst' % i, 'w').write(nodeb[i])
			nb = Parser('tests\\cmpb%i.tst' % i).read()
			na.sumSameFactors()
			self.assertEqual(Node.compare(na, nb), True)
			file('tests\\cmpbb%i.tst' %(nTests - i - 1), 'w').write(nodeb[nTests - i - 1])
			nb = Parser('tests\\cmpbb%i.tst' % (nTests - i - 1)).read()
			self.assertEqual(Node.compare(na, nb), False)
			
	def test_suppress_imaginary_units(self):
		nTests = 4
		nodea = ['a + jX', 'a - jjXy', 'a + jjjj(b+3j)j',  'jjjj']
		nodeb = ['a + jX', 'a + Xy', 'a + (b+3j)j',  '1']
		for i in range(0, nTests):
			print 'test pass', i
			na = self.loadFromString(nodea[i])
			nb = self.loadFromString(nodeb[i])
			na.suppressImaginary()
			self.assertEqual(Node.compare(na, nb), True)
			
	def test_point_out(self):
		nTests = 5
		nodea = ['ab+(ca+bc)', 'ajD(aa+ba-1)', 'a+1-ba-bb', 'a+b', 'b+c']
		nodeb = ['a(b+c)+bc', 'ajD(a(a+b)-1)', '1+a(1-b)-bb', 'a+b', 'b+c']
		for i in range(0, nTests):
			print 'test pass', i
			na = self.loadFromString(nodea[i])
			nb = self.loadFromString(nodeb[i])
			na.pointOut('a')
			self.assertEqual(Node.compare(na, nb), True)
		
		

class TestMath2(TestCase):
	def setUp(self):
		pass
	
	def tearDown(self):
		pass
		
	def test_1(self):
		pass

testCases = [TestMath, TestMath2]

suite = TestSuite()
for case in testCases:
	partsuite = TestLoader().loadTestsFromTestCase(case)
	suite.addTest(partsuite)
TextTestRunner(verbosity=2).run(suite)
