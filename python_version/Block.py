
class Block:


	def __init__(self):
		var = []

	def __init__(self, statement):
		self.var.append(statement)

	def add(self):
		if self.var == None:
			raise ValueError("null statement argument")
		self.var.append(self.statement)

	def process(self):
		for x in range(0, self.var.size()):
			self.var.get(x).execute()

	def size(self):
		return self.var.size()