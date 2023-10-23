student = {'name': 'Jhon', 'age' : '23' , 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])
print(student['courses'])


student1 = {1: 'Jhon', 'age' : '23' , 'courses': ['Math', 'CompSci']}
print(student1[1])

# print(student1['phone'])
print(student.get('name'))

#If the value doesnt exist, returns "not found"
print(student.get('phone', 'Not found'))

student['phone'] = '617 17 90 86'
student['name'] = 'Jhonny'
print(student)

student.update({'name':'Jane', 'age':'26', 'phone': "267 239 122"})
print(student)

age = student.pop('age')
#del student['age']
print(student)
print(age)

print(len(student))
print(student.keys())
print(student.items())


for key in student:
    print(key)
    
for key,value in student.items():
    print(key, value)