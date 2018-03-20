#!/usr/bin/env python3

import json
courses = { 1:'Linux', 2:'Vim', 3:'Git'}
json.dumps(courses)

print(json.dumps(courses))

with open('courses.json', 'w') as file:
    file.write(json.dumps(courses))

with open('courses.json', 'r') as file:
    new_courses = json.loads(file.read())
print(new_courses)


print(type(courses))


