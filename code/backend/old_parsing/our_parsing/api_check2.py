#!/user/bin/env python3

from concurrent.futures import process
from urllib import response
from urllib.parse import scheme_chars
from venv import create

from models import Course
# from django.db import models
# from api.serializers import CourseSerializer


import requests
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

# API_URL = "https://sis.jhu.edu/api/classes/codes/schools"
API_URL = "https://sis.jhu.edu/api/classes"

response = requests.get(API_URL, params={"key": 'rZW4VwAUE1WTYZfSZyldykJLOXUC59fr'})

# Convert json to dict
data = json.loads(response.text)

# Convert dict to string
data = json.dumps(data)
# print(data) --> [[{"Message": "Please specify a search or use filters"}]]

### get all possible terms ###
terms = []
terms_request = json.loads(requests.get(API_URL + '/codes/terms', params={"key": 'rZW4VwAUE1WTYZfSZyldykJLOXUC59fr'}).text)
for term in terms_request:
    terms.append(term['Name'])

# print(terms)

### get all possible schools ###
schools = []
schools_request = json.loads(requests.get(API_URL + '/codes/schools', params={"key": 'rZW4VwAUE1WTYZfSZyldykJLOXUC59fr'}).text)
for school in schools_request:
    schools.append(school['Name'])

### get all possible departments for school ###
# depts_by_school = {}

# for school in schools:
#     departments_request = json.loads(requests.get(API_URL + '/codes/departments/' + school.replace(" ", "%20") , params={"key": 'rZW4VwAUE1WTYZfSZyldykJLOXUC59fr'}).text)
#     depts = []
#     for dept in departments_request:
#         depts.append(dept['DepartmentName'])
#     depts_by_school[school] = depts


### get all courses for all schools ###

# for school in schools:
#     course_request = json.loads(requests.get(API_URL + '/codes/departments/' + school.replace(" ", "%20") , params={"key": 'rZW4VwAUE1WTYZfSZyldykJLOXUC59fr'}).text)

### get all courses for all schools for specific term ###

term = terms[6]
courses_by_school = {}
for school in schools:
    # print(school, '\n')
    # print(term, '\n')
    # course_request = json.loads(requests.get(API_URL + '/' + school.replace(" ", "%20") + '/' + term.replace(" ", "%20"), params={"key": 'rZW4VwAUE1WTYZfSZyldykJLOXUC59fr'}).text)
    course_request = json.loads(requests.get(API_URL + '/AS01052211/' + 'Spring%202022', params={"key": 'rZW4VwAUE1WTYZfSZyldykJLOXUC59fr'}).text)

    courses = []

    for course in course_request:
        c = {}
        if (course['SchoolName'] != school):
            courses.append(c)
            continue
        c['name'] = course['Title']
        c['description'] = course['SectionDetails'] # ?
        c['course_num'] = course['OfferingName']
        c['num_credits'] = str(course['Credits']) # not necessairly a number
        c['department'] = course['Department']
        c['level'] = course['Level']
        c['prerequisites'] = course['SectionRegRestrictions'] # string list
        c['corequisites'] = course['SectionCoRequisites']
        c['school'] = course['SchoolName']
        c['campus'] = course['Location']
        c['is_writing_intensive'] = True if(course['IsWritingIntensive'] == 'Yes') else False
        c['meeting_section'] = course['SectionName']
        # c['size'] = 
        c['instructors'] = course['InstructorsFullName']
        c['semester'] = course['Term'].split(' ')[0] + course['Term'].split(' ')[1] # grab first word of term

        courses.append(c)
        test_model = Course.create(c)
        #     print(course)
    courses_by_school[school] = courses

    # print(courses_by_school)

print(test_model)

# pretty_print_json = pprint.pformat(json.dumps(courses_by_school)).replace("'", '"')

# with open('result.json', 'w') as f:
#     json.dump(courses_by_school, f, indent=4)
#     # f.write(pretty_print_json)



# pp.pprint(courses_by_school)


### testing model creation with one class ###




### create json from dict ###



### UPLOADING TO DJANGO: create models from json ###



# json_response = response.json()
# str_response = json.dumps(json_response)


# with open(data, 'r') as j:
#      contents = json.loads(j.read())
#      print(contents)

# response.raise_for_status()


# if (
#     response.status_code != 204 and
#     response.headers["content-type"].strip().startswith("application/json")
# ):
#     try:
#         print('here')
#         print(json.dumps(response.json()))
#     except ValueError:
#         # decide how to handle a server that's misbehaving to this extent
#         print("ugh")

# print(json.dumps(json_response))