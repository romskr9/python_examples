from mymath import *

class Parser:
	
	def __init__(self, name = None):
		self.init(name)
			
	def init(self, name = None):
		self.token = None
		self.one = None
		if name:
			self.name = name
			self.f = file(name, 'r')
			
	def getone(self):
		if self.one:
			result = self.one
			self.one = None
#			print 'got one char from buffer', result
			return result
		else:
			result = self.f.read(1)
#			print 'read one char from file', result, len (result)
			return result
			
			
	def putone(self, one):
		self.one = one
			
	def get(self):
		if self.token:
			result = self.token
			self.token = None
			return result
		else:
			c = self.getone()
			while c.isspace():
				c = self.getone()				
			if c == '':
				return 'end'
			elif c.isupper():
				result = c
				c = self.getone()
				while c.islower():
					result += c
					c = self.getone()
				self.putone(c)
				return result
			elif c.islower() or c in '+-*()':
				return c
			elif c.isdigit():
				result = c
				c = self.getone()
				while c.isdigit():
					result += c
					c = self.getone()
				self.putone(c)
				return result
			else:
				print 'error>>', c
					
	def put(self, token):
		self.token = token
	
	def read(self):
		return self.readSum()
		token = self.get()
		
	def readSum(self):
		token = self.get()
		if token != '-':
			self.put(token)
		n1 = self.readProduct()
		if token == '-':
			n1.multiplewith(-1)
		if n1 is not None:
			token = self.get()
			if token in ['+', '-']:
				n = Node('+')
				n.data.append(n1)
				while token in ['+', '-']:
					n2 = self.readProduct()
					if token == '-':
						n2.multiplewith(-1)
					n.data.append(n2)					
					token = self.get()
				self.put(token)				
				return n
			else:
				self.put(token)
				return n1
		else:
			return n1
			
	def readProduct(self):
		n1 = self.readAtom()
		if n1 is not None:
			token = self.get()
			self.put(token)
			if token not in ['+', '-', ')', 'end']:
				n = Node('*')
				n.data.append(n1)
				while token not in ['+', '-', ')', 'end']:
					n2 = self.readAtom()
					n.data.append(n2)					
					token = self.get()
					self.put(token)				
				return n
			else:
				return n1
		else:
			return n1

	def readAtom(self):
		token = self.get()
		if token.isalpha():
			n = Node('A', token)
			return n		
		elif token.isdigit():
			n = Node('D', int(token))
			return n		
		elif token == '(':
			n = self.readSum()
			token = self.get()
			return n

