#!/home/birac/anaconda2/bin/python

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

