from sys import *

class Node:
	def __init__(self, type, data = None):
		self.type = type
		self.data = []
		if data is not None:
			self.data = [data]
		
	def len(self):
		return len(self.data)
		
	def multiplewith(self, mult):
		if self.type == '*':
			ok = False
			for i in range(0, self.len()):
				if self.data[i].type == 'D':
					self.data[i].data[0] *= mult
					ok = True
					break
			if not ok:
				self.data.append(Node('D', mult))
		elif self.type == 'D':
			self.data[0] *= mult
		else:
			n = Node(self.type)
			n.data = self.data
			self.type = '*'
			self.data = [Node('D', mult), n]
			
	def isnegative(self):
		if self.type == 'D':
			return self.data[0] < 0
		elif self.type == '*':
			result = False
			for i in range(0, self.len()):
				if self.data[i].isnegative():
					result = not result
			return result
		else:
			return False
			
	def writeout(self, f, minus = 1):
		theFirst = True
		if self.type == '+':
			for i in range(0, self.len()):
				neg = self.data[i].isnegative()
				if neg:
					f.write('-')
					self.data[i].writeout(f, minus = -1)
				else:
					if not theFirst:
						f.write('+')
					self.data[i].writeout(f)
				theFirst = False
		elif self.type == '*':
			for i in range(0, self.len()):
				product = 1
				if self.data[i].type == 'D':
					product *= self.data[i].data[0]
				if abs(product) != 1:
					self.data[i].writeout(f, minus = minus)					
			for i in range(0, self.len()):
				if self.data[i].type == '+':
					f.write('(')
					self.data[i].writeout(f)
					f.write(')')
				elif not self.data[i].type == 'D':
					self.data[i].writeout(f)
		elif self.type == 'D':
			f.write('%i' %(minus * self.data[0]))
		else:
			f.write(self.data[0])
			
	def debug(self, f = stdout):
		self.dbg(0, f)
		
	def dbg(self, tab, f):
		f.write(tab*'\t' + self.type + ':')
		if self.type in 'AD':
			f.write(str(self.data) + '\n')
		else:
			f.write('\n')
			for i in range(0, self.len()):
				self.data[i].dbg(tab + 1, f)
		
	def normalize(self, alwaysNum = False):
		if self.type in '+*':
			rslt = 0
			if self.type == '*':
				rslt = 1
			simples = []
			complexes = []
			i = 0
			while i < self.len():
				item = self.data[i]
				if item.type in '*+':
					item.normalize()
					if self.type == item.type:
						self.data += item.data
						del self.data[i]						
						i -= 1
				i += 1
			for item in self.data:
				if item.type == 'A':
					if self.type == '+' and alwaysNum:
						newItem = Node('*')
						newItem.data = [Node('D', 1), item]
						complexes.append(newItem)
					else:
						simples.append(item)
				elif item.type in '+*':
					complexes.append(item)
				elif self.type == '*':
					rslt *= item.data[0]
				else:
					rslt += item.data[0]
			simples.sort(key = lambda x: x.data[0])
			complexes.sort(key = lambda x: x.size())
			self.data = []
			if self.type == '*' and (rslt != 1 or alwaysNum == True ) or self.type == '+' and rslt != 0:
				self.data = [Node('D', rslt)]
			self.data += simples + complexes
			if self.len() == 1:
				self.type = self.data[0].type
				self.data = self.data[0].data
			

	def multout(self):
		if self.type in '*+':
			self.normalize()
			for item in self.data:
				item.multout()
			self.normalize()
		if self.type == '*':
			pos = 0
			for i in range(self.len()):
				if self.data[i].type in 'AD':
					pos += 1
			result = [self.data[:pos]]
			if pos == 0:
				result = [[Node('D', 1)]]
			while pos < self.len():
				baseSum = result
				result = []
				for item1 in baseSum:
					for item2 in self.data[pos].data:
						product = Node('*')
						product.data = item1 + [item2]
						product.normalize()
						if product.type == '*':
							result.append(product.data)
						else:
							result.append([product])
				pos +=1
			self.type = '+'
			self.data = []
			for item in result:
				self.data.append(Node('*'))
				self.data[-1].data = item
			self.normalize()

	def size(self):
		result = 1
		if self.type in '+*':
			for item in self.data:
				result += item.size()
		return result
		
	def compare(self, node, respect = True):
		self.normalize(alwaysNum = True)
		node.normalize(alwaysNum = True)
		if self.type != node.type:
			result = False
		elif self.type in 'AD':
			result = self.data == node.data
		elif self.len() != node.len():
			result = False
		else:
			result = True
			if self.type == '*' and not respect:
				for i in range(1, self.len()):
					if not self.data[i].compare(node.data[i]):
						result = False
						break
			else:
				for i in range(self.len()):
					if not self.data[i].compare(node.data[i], respect):
						result = False
						break
		#~ self.normalize()
		#~ node.normalize()
		return result
		
	def sumSameFactors(self ):
		self.normalize(alwaysNum = True)
		if self.type == '+':
			i = 0
			while i < self.len() -1:
				j = i + 1
				while j < self.len():
					if Node.compare(self.data[i], self.data[j], respect = False):
						self.data[i].data[0].data[0] += self.data[j].data[0].data[0]
						del self.data[j]
						j -= 1
					j += 1
				if self.data[i].data[0].data[0] == 0:
					del self.data[i]
					i -= 1
				i += 1
			if self.len() == 0:
				self.type = 'D'
				self.data = [0]

	def suppressImaginary(self, img = 'j'):
		if self.type == '*':
			oldLen = self.len()
			self.normalize()
			i = 0
			while i < self.len():
				if self.data[i].type == 'A' and self.data[i].data[0] == img:
					del self.data[i]
					i -=1
				else:
					self.data[i].suppressImaginary()
				i+=1
			cnt = oldLen - self.len()
			cnt %= 4
			arr = []
			if cnt in [1, 3]:
				arr.append(Node('A', img))
			if cnt in [2, 3]:
				arr.append(Node('D', -1))
			self.data += arr
			self.normalize()
		elif self.type == '+':
			self.normalize()
			for item in self.data:
				item.suppressImaginary()
		
	def pointOut(self, var):
		self.normalize()
		if self.type in '*+':
			for item in self.data:
				item.pointOut(var)
		self.normalize()
		if self.type == '+':
			result = []
			i = 0
			while(i < self.len()):
				if self.data[i].type == '*':
					found = False
					for j in range(self.data[i].len()):
						found = self.data[i].data[j].type == 'A' and self.data[i].data[j].data[0]  == var
						if found:
							break
					if found:
						del self.data[i].data[j]
						result.append(self.data[i])
						del self.data[i]
						i -= 1
				elif self.data[i].type == 'A' and self.data[i].data[0] == var:
					result.append(Node('D', 1))
					del self.data[i]
					i -= 1
				i +=1
			if result:
				item = Node('*')
				item.data = [Node('A', var), Node('+')]
				item.data[1].data = result
				self.data.append(item)
				self.normalize()
