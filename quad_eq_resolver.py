"""
Quadratic equation solver
Théo Tchilinguirian 2019
"""

# Imports :
from math import *


# Functions :

def sign(x):
	"""
	Returns a float's sign as a string.
	"""
	return '+' if x>= 0 else '-'


def solve(a, b, c):
	"""
	Prints the solutions of f(x) = 0
	Not a very dynamically written function. >:( (not that I got the time for it)
	"""
	delta = b**2 - 4*a*c
	print(delta)

	if delta < 0:
		print("the equation has no real solution.")
	elif delta > 0:
		# 2 real solutions
		x1 = (-1*b + sqrt(delta))/(2*a)
		x2 = (-1*b - sqrt(delta))/(2*a)
		print("The solutions for f(x) = 0 are", x1, " and", x2)
		else:
		# 1 real solutions
		x0 = sqrt(delta)/(2*a)
		print("The solution for f(x) = 0 is", x0)


def sign_table(a, b, c):
	"""
	Prints the sign table of f(x)
	Not a very dynamically written function. >:( (competing for most horrendous code)
	"""
	delta = b**2 - 4*a*c
	if delta > 0:
		x1,x2=(-1*b + sqrt(delta))/(2*a),(-1*b - sqrt(delta))/(2*a)
	elif delta == 0 :
		x0=sqrt(delta)/(2*a)
	
	if delta > 0:
		if a > 0:
			print("""
			x   |-inf     x1     x2     +inf|
			---------------------------------
			f(x)|     +    0  -  0    +     |
			""")

		if a < 0:
			print("""
			x   |-inf     x1     x2     +inf|
			---------------------------------
			f(x)|     -    0  +  0    -     |
			""")
	if delta == 0:
		if a > 0:
			print("""
			x   |-inf         x0        +inf|
			---------------------------------
			f(x)|     +       0       +     |
			""")

		if a < 0:
			print("""
			x   |-inf         x0        +inf|
			---------------------------------
			f(x)|     -       0       -     |
			""")
	
def var_table(a, b, c):
	"""
	Prints the variation table of f(x)
	Not a very dynamically written function. >:( (need to sleep)
	"""
	delta = b**2 - 4*a*c
	r = (-1*b)/(2*a)  # Solution of f'(x) = 0

	if delta > 0:
		if a > 0:
			print("""
			x    |-inf      -b/2a        +inf|
			----------------------------------
			f(x) |     dec    |     inc      |
			f'(x)|      -     0      +       |
			""")

		if a < 0:
			print("""
			x    |-inf      -b/2a        +inf|
			----------------------------------
			f(x) |     inc    |     dec      |
			f'(x)|      +     0      -       |
			""")


def main():
	"""
	The main function loop.
	"""
	
	print("This program solves equations like the following : xa^2 + bx + c = 0 for real solutions only.", end='\n')
	
	resolving_equations = True
	while resolving_equations:
	
		cond = True
		while cond:
			try:
				a = float(input("Enter the quadratic coefficient of your equation: "))
				b = float(input("Enter the linear coefficient of your equation: "))
				c = float(input("Enter the constant term of your equation: "))

				cond = False
				break

			except:
				print("Coefficients must be real numbers.")
				continue

			print("f(x) =", sign(a) + str(sqrt(a**2)) + "x²", sign(b) + " " + str(sqrt(b**2)) + "x", sign(c) + " " + str(sqrt(c**2)))
			
			choosing = True
			while choosing:
				print("""Choose an option:
				1. Solve f(x) = 0
				2. Get variation table
				3. Get variation table
				3. Stop
				""")
				try:
					opt = int(input("Choose an option: "))
					if opt == 1:
						solve(a, b, c)
					elif opt == 2:
						sign_table(a, b, c)
					elif opt == 3:
						var_table(a, b, c)
					elif opt == 3:
						print("Bye.")
					else :
						print("Choose a number between 1 and 4")
						continue
					choosing = False
					break
				except:
					print("Invalid choice")
					continue


# Main :
		
main()

