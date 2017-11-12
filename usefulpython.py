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

# Print run time of script
print datetime.now() - startTime

