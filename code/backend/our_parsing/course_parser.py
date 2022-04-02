#!/user/bin/env python3

from concurrent.futures import process
from urllib import response
from urllib.parse import scheme_chars
from venv import create

from course.models import Course

import requests
import json

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('school', type = str)
parser.add_argument('term', type = str)

args = parser.parse_args()

print(args)

API_URL = "https://sis.jhu.edu/api/classes"

# check valid term
terms = ['Spring 2023', 'Intersession 2023', 'Fall 2022', 'Summer 2022', 'Spring 2022', 'Intersession 2022', 'Fall 2021', 'Summer 2021', 'Spring 2021', 'Intersession 2021', 'Fall 2020', 'Summer 2020', 'Spring 2020', 'Intersession 2020', 'Fall 2019', 'Summer 2019', 'Spring 2019', 'Intersession 2019', 'Fall 2018', 'Summer 2018', 'Spring 2018', 'Intersession 2018', 'Fall 2017', 'Summer 2017', 'Spring 2017', 'Intersession 2017', 'Fall 2016', 'Summer 2016', 'Intersession 2016', 'Spring 2016', 'Fall 2015', 'Summer 2015', 'Intersession 2015', 'Spring 2015', 'Fall 2014', 'Summer 2014', 'Spring 2014', 'Intersession 2014', 'Fall 2013', 'Summer 2013', 'Intersession 2013', 'Spring 2013', 'Fall 2012', 'Summer 2012', 'Spring 2012', 'Intersession 2012', 'Fall 2011', 'Summer 2011', 'Intersession 2011', 'Spring 2011', 'Fall 2010', 'Summer 2010', 'Spring 2010', 'Intersession 2010', 'Fall 2009', 'Summer 2009', 'Spring 2009']

if !(args.term in terms) :
    print("Invalid term")

# check valid school
schools = ['Bloomberg School of Public Health', 'Bloomberg School of Public Health Non-Credit', 'Carey Business School', 'Krieger School of Arts and Sciences', 'Krieger School of Arts and Sciences Advanced Academic Programs', 'Nitze School of Advanced International Studies', 'School of Education', 'School of Medicine', 'School of Nursing', 'The Peabody Institute', 'The Peabody Preparatory', 'Whiting School of Engineering', 'Whiting School of Engineering Programs for Professionals']

if !(args.school in schools) :
    print("Invalid school name")

# grab all courses for school and term

course_request = json.loads(requests.get(API_URL + '/' + args.school.replace(" ", "%20") + '/' + args.term.replace(" ", "%20"), params={"key": 'rZW4VwAUE1WTYZfSZyldykJLOXUC59fr'}).text)

for course in course_request:
    c = json.loads(requests.get(API_URL + '/' + course["OfferingName"].replace(".", "") + course["SectionName"] + '/' + args.term.replace(" ", "%20"), params={"key": 'rZW4VwAUE1WTYZfSZyldykJLOXUC59fr'}).text)


    try :
        prereq = c["SectionDetails"][0]["Prerequisites"][0]["Description"]
    except:
        prereq = ''

    try:
        coreq = c["SectionDetails"][0]["CoRequisites"][0]["Description"]
    except:
        coreq = ''

    course_model = Course(
            name=c["Title"],
            description=c["SectionDetails"],
            course_num=c["OfferingName"],
            num_credits=c["Credits"],
            department=c["Department"],
            level=c["Level"],
            prerequisites=prereq,
            corequisites=coreq,
            school=c["SchoolName"],
            campus=c["Location"],
            is_writing_intensive=True
            if (c["IsWritingIntensive"] == "Yes")
            else False,
            meeting_section=c["SectionName"],
            instructors=c["InstructorsFullName"],
            semester=(
                c["Term"].split(" ")[0] + " " + c["Term"].split(" ")[1]
            ),
        )
    course_model.save()