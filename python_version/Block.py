
class Block:

	ar = []

	def __init__(self, statement):
		self.ar.append(statement)

	def add(self,statement):
		if self.ar == None:
			raise ValueError("null statement argument")
		self.ar.append(statement)

	def process(self):
		for x in range(0, len(self.ar)):
			self.ar[x].execute()

	def size(self):
		return len(self.ar)