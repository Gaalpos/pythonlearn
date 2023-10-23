courses = ['history', 'math', 'physics', 'art']
print(len(courses))

print(courses)
print(courses[1])

#last index
print(courses[-1])

#index number 2 not included
print(courses[0:2])
print(courses[:2])

print(courses[2:])

courses.append('football')
print(courses)

courses.insert(0, 'sport')
print(courses)

courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print (courses)

courses.extend(courses_2)
print(courses)

courses.remove('math')
print(courses)

#removes last index
courses.pop()
print(courses)

popped = courses.pop()
print (popped)

courses.reverse()
print(courses)

courses = ['history', 'math', 'physics', 'art']
courses.sort()
print(courses)


nums = [ 1, 8 , 3, 4 ]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

sorted_list = sorted(courses)
print(sorted_list)

print(min(nums))
print(max(nums))
print(sum(nums))


print(courses.index('math'))
# value error : print(courses.index('mates'))

print('art' in courses)
print('artes' in courses)

print('all the courses:')
for item in courses:
    print (item)
    
for index, course in enumerate(courses):
    print (index, course)

for index, course in enumerate(courses, start=1):
    print (index, course)


course_string = ', '.join(courses)
print (course_string)

course_string = ' - '.join(courses)
print (course_string)

new_list = course_string.split(' - ')
print(new_list)
















