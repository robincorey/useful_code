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
