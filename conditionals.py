# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is



if True:
    print('Conditinal was true')

if False:
    print('Conditinal was true')


language = 'Python'

if language == 'Python':
    print (' we are using python ')
language = 'Java'


if language == 'Python':
    print (' we are using python ')
else :
    print('no match')
    

if language == 'Python':
    print (' we are using python ')
elif language == 'Java':
    print('we are using Java')

else :
    print('no match')
     

user = 'Admin' 
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad credentials')

user = 'Admin' 
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad credentials')
    
if user == 'Admin' or logged_in:
    print('Admin page')
else:
    print('Bad credentials')

if not logged_in:
    print('please log in')
else:
    print('welcome')

a = [1, 2 ,3]
b = [1, 2 ,3]

# equals check if the values are the same
print (a == b )

# is check i they are the SAME objects on memory
print (a is b )

b = a

print(id(a))
print(id(b))
print(id(a) == id(b))

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

conditon = True
if conditon:
    print ('true')
else :
    print('false')

conditon = None
if conditon:
    print ('true')
else :
    print('false')
 