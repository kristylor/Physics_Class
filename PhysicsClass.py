"""
Getting Ready for Physics Class
You are a physics teacher preparing for the upcoming semester.
You want to provide your students with some functions that will
help them calculate some fundamental physical properties.
"""

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:
#takes an input temperature in Fahrenheit, and converts it to a temperature in Celsius.
def f_to_c(f_temp):
  return (f_temp - 32) * 5 / 9

#esting function with a value of 100 Fahrenheit
f100_in_celsius = f_to_c(100)
print(round(f100_in_celsius, 2))

#takes an input temperature in Celsius, and converts it to a temperature in Fahrenheit.
def c_to_f(c_temp):
  return c_temp * (9 / 5) + 32

#testing function with a value of 0 Celsius
c0_in_fahrenheit = c_to_f(0)
print(round(c0_in_fahrenheit, 2))

#function that takes in mass & acceleration & return mass * acceleration
def get_force(mass, acceleration):
  return mass * acceleration

#testing get_force
train_force = get_force(train_mass, train_acceleration)

print(f"The GE train supplies {train_force} Newtons of force")

#function that takes in mass and c. c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. get_energy should return mass multiplied by c squared.
def get_energy(mass, c=3*10**8):
  return mass * c**2

#testing get_energy
bomb_energy = get_energy(bomb_mass)

print(f"A 1kg bomb supplies {bomb_energy} Joules.")

#function that takes in mass, acceleration, and distance. Work is defined as force multiplied by distance. First, get the force using get_force, then multiply that by distance. Return the result.
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

#testing get_work
train_work = get_work(train_mass, train_acceleration, train_distance)

print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")
