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

