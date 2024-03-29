# Record time that script starts
startTime = datetime.now()

# To allow matplotlib to run remotely
import matplotlib
matplotlib.use('Agg')

# Better than os.system
sed = subprocess.call(['sed', '/#/d', filename], stdout=f)

# To remove chars from end
var = "1234.xvg"
strip_var = var.rstrip('.xvg')

# To remove chars from whole thing
var = "H@e@ll@o"
repl_var = var.replace('@','')
#or
def anti_vowel(text):
  vowels = ['A','E','I','O','U','a','e','i','o','u']
  for v in vowels:
    text = text.replace(v,'')
  return text

del anti_vowel # delete a function.

# Lists 
my_list = [1, "Hello", 3.4]
print(my_list[2:3]) # print range
mylist[2] = "Goodbye" # change val
mylist.append("end") # append
len(my_list)
for index, item in enumerate(my_list): # To enumerate - i.e. add index to list
  print index+1, item

my_list2 = [3, 5, 9]

for a, b in zip(my_list, my_list): # iterate two lists
  print a, b
  
# check if number even
def is_even(x):
  ''' Notes here. This shows up in the 'help section '''p
  if x % 2 == 0:
    return True
  else:
    return False

# check for integer
import decimal
def is_int (x):
  num = round(x,0)
  if num == x:
    print "round"
    return True
  else:
    print "not round"
    return False

# perform factorial
def factorial (x):
  fact = 1
  for i in range(x):
    fact = (i+1) * fact
    print fact
  return fact

# reverse string
def reverse (text):
  word = []
  for c in text:
    word = [c] + word
  revword = ''.join(word)
  print revword
  return revword

reverse('hello')

# Print run time of script
print datetime.now() - startTime

# define dictionary
dictionary = {
  "simname": "WT_ADP",
  "length": 500,
}

print my_dict.items() # items=all items, keys=list of key, values=list of vals
for key in my_dict:
  print key, my_dict[key]
  
# list comprehension
even_squares = [i ** 2 for i in range(1,11) if i % 2 == 0]

backwards = my_list[::-1]

# Functional programming
# partly from http://book.pythontips.com/en/latest/map_filter.html
# Lambda creates anonymous (nameless) function
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)
# = [0, 3, 6, 9, 12, 15]
# "def" better for functions used many times
# filter creates a list of elements for which a function returns true. Resembles a loop.
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list)) #same as saying "if x<0" but quicker and nicer

# Map applies a function to all the items in an input_list.
map(function_to_apply, list_of_inputs)
# so, you can make certain code simpler
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
# becomes
items = [1, 2, 3, 4, 5]

# Reduce is a  function for performing some computation on a list and returning the result.
# old =
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
# list converts iterable to list, map applies function to each iterable item, and lambda is an anon function saying x**2
# map often used with lambda

# same as   
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
squared = list(map(lambda x: x**2, items))

# Bitwise operators - operations that manage bits of info
print 0b1, # 0b means binary, 1 means 1
print 0b111, # 111 = 7 , one four, one two and one one
print bin(5) # print the binary of an integer oct(5) and hex(5) work too
print int("0b100",2) # second parameter refers to the base the number is in (10 default)
shift_right = 0b1100 >> 2  # =0b11 shifts your binary number left or right
print bin(0b1110 & 0b101) # =0b100 returns 1 if both numbers 1 in that position. Can do or too (|) or exclusive or (^)

#### Classes - important to OOP. Class is a way of organizing and producing objects with similar attributes and methods
class NewClass(object):  # new class (use Caps), which inherits from the 'object' class
  ''' Add documentation here
      Blah blah blah
  '''
  member_variable = "Hello"             # Define "member variables" available to this class only (i.e. not global variables). All members have this
  def __init__(self, name, age)         # Constructor: initializes object. always start with self, then add other tings. Self will = name of described object. DON'T NEED/
    ''' Add documentation about constructor here
        Blah blah blah
    '''                                 # The first argument passed to __init__() must always be the keyword self - this is how the object keeps track of itself internally 
    self.name = name                    # create an instance object. We assign a variable (name) to the class (via self) = new member variable
    self._name = name                   # underscore "hides" variable for security. Stops it being changed.
    self.age = age
  def description(self):                # Can define own methods. __init__ is a method, so is this
    ''' Document member functions here
    '''
    print self.name
    print self.age
  
hippo = Animal("Poupe", 3)              # To call bespoke method. Now hippo=self
print hippo.name                        # will print Poupe
print hippo.member_variable             # will be Hello by default for every new Animal. This is a member variable - all members of this class have this value
hippo.member_variable = "Goodbye"       # This will ONLY change the member variable for hippo, not other Animals

hippo.description() # to call bespoke method

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
    
  def display_car(self):
    m = str(self.mpg)
    return "This is a %s %s with %s MPG." % (self.color, self.model, m)
  def drive_car(self):
    self.condition = "used"
  
my_car = Car("DeLorean", "silver", 88)

print my_car.display_car()
print my_car.condition
my_car.drive_car()
print my_car.condition # changes from new to used

# Inheritance is the process by which one class takes on the attributes and methods of another, and it's used to express an is-a relationship. 

class InheritedClass(BaseClass):    # declare class to inherit from in brackets

class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type): # need to define al variables again
    self.model = model                                  # need to define all this crap again
    self.color = color
    self.mpg = mpg 
    self.battery_type = battery_type
    
my_car = ElectricCar("Honda", "blue", 100, "molten salt")

# I/O

my_list = [i ** 2 for i in range(1, 11)]
my_file = open("output.txt", "w")
for i in my_list:
  istr = str(i)
  my_file.write(istr + "\n")
my_file.close()    # otherwise python doesn't flush the buffer - i.e might not write to the file

my_file = open("output.txt","r")
print my_file.read()
my_file.close()

with open("text.txt", "w") as textfile:  # this invokes autoexit. No need for closing.
  textfile.write("Success!")

# From Data python workshop 07/12/17

letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.',
                   'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--',
                   'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                   'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                   '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   ' ':'/' }
message = "SOS We have hit an iceberg and need help quickly"
morse = []
for letter in message:
    morse.append(letter_to_morse[letter.lower()])
    
#small change
    
print(morse)

class Morse:
    def __init__(self):
        self._letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', ## _ before letter prevents changes
                   'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--',
                   'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                   'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                   '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   ' ':'/' }
        
    def encode(self, message):
        morse = []
        for letter in message:
            morse.append( self._letter_to_morse[letter.lower()] )
        return morse
      
# Exceptions!
def setHeight(height):
    if height < 0 or height > 300:
        raise ValueError("Invalid height: %s. This should be between 0 and 300" % height)
        
    print("Height is set to %s" % height)
def setHeight(height):
    if height < 0 or height > 300:
        raise ValueError("Invalid height: %s. This should be between 0 and 300" % height)
        
    print("Height is set to %s" % height)
ValueError
IOError
ZeroDivisionError
TypeError
IndexError
KeyError

# try/except
def setHeight(height):
    try:
        height = float(height)
    except:
        raise TypeError("Invalid height: '%s'. You can only set the height to a numeric value" % height)

# else gives and else option for except
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
        
#regex
import re
^\s*(\d+\.?\d*)\s*(kg|kilogram?)\s*$
https://regex101.com/
  
# List items are ordered, changeable, and allow duplicate values
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Set items are unordered, unchangeable, and do not allow duplicate values.

# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# to ignore order of arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# function with default parameter
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
