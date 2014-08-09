import vector
import copy

class Body:
	def __init__(self, position=vector.Vector(), velocity=vector.Vector(), mass=0):
		self.position = position
		self.velocity = velocity
		self.mass = mass
		
	def update(self, others, dt):
		accel = vector.Vector()
		for particle in others:
			dist = (particle.position-self.position)/100
			grav = (particle.mass/(abs(dist)**3))*dist
			accel = accel + grav
		self.position = self.position + (self.velocity*dt)
		self.velocity = self.velocity + (accel*dt)

def collide(body1, body2):
	p_in = (body1.mass*body1.velocity)+(body2.mass*body2.velocity)
	coord_vel = p_in/(body1.mass + body2.mass)
	rel_pos = body1.position - body2.position
	normal = rel_pos/abs(rel_pos)
	vel1 = body1.velocity-coord_vel
	vel2 = body2.velocity-coord_vel
	u1 = (vel1 - (2*vel1*normal)*normal)
	u1 = u1/abs(u1)
	u2 = -1*u1
	k_in = (body1.mass*(vel1*vel1)) + (body2.mass*(vel2*vel2))
	elasticity = 0.75
	scale2 = elasticity*((k_in*body1.mass)/((body2.mass**2) + body2.mass*body1.mass))**0.5
	scale1 = (body1.mass/body2.mass)*scale2
	out1 = copy.copy(body1)
	out1.velocity = (u1*scale1)+coord_vel
	out2 = copy.copy(body2)
	out2.velocity = (u2*scale2)+coord_vel
	out1.position = out1.position+(out1.velocity*0.1)
	return (out1, out2)
