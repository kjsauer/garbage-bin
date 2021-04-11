# Make strings in Python
A = 'Cat'
B = 'Dog'
C = '3'
# Method 1
make_string_1 = '%s\n%s\n%s'%(A,B,C)
# Print string result of Method 1
print(make_string_1)
# Method 2
make_string_2 = '''%s
%s
%s'''%(A,B,C)
# Print string result of Method 2
print(make_string_2)
# One input only
make_string_3 = '%s'%A
print(make_string_3)