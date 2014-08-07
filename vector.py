class Vector:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def __add__(self, other):
		return Vector(self.x+other.x, self.y+other.y)
	
	def __sub__(self, other):
		return Vector(self.x-other.x, self.y-other.y)
	
	def __mul__(self, other):
		if isinstance(other, Vector):
			return (self.x*other.x)+(self.y*other.y)
		else:
			return Vector(self.x*other, self.y*other)
	
	def __rmul__(self, scalar):
		return Vector(self.x*scalar, self.y*scalar)
	
	def __abs__(self):
		return (self*self)**0.5
