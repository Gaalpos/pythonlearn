# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math','Sport'}
art_courses = {'History', 'Math', 'Physics', 'Art', 'Design'}


print(cs_courses)
print('Math' in cs_courses)

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

