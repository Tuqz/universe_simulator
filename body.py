import vector

class Body:
	def __init__(self, position=vector.Vector(), velocity=vector.Vector(), mass=0):
		self.pos = position
		self.velocity = velocity
		self.mass = mass
