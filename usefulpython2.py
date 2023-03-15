# Follow up tips for better coding

# f strings for printing strings

a = 'there'
b = 'ugly'

print(f"hi {a} you are very {b}")

# better looping

a = [1, 2, 3]

# old and ugly
for i in range(len(a)):
	print(i)

# new and swish
for i in a:
	print(i)


# classes

class Employee:
	def __init__(self, first, last, email, pay): # make instance first arg
		# define attributes
		self.first = first
		self.last = last
		self.email = first + ‘.’ last + ‘@companyname.com’
		self.pay = pay
	def full_name(self):
		return ‘{} {}’.format(self.first, self.last) # def method

emp_1 = Employee(‘doodie’, ‘poodie’, 50000)
print(emp_1.full_name())

