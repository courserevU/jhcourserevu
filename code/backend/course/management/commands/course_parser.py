from course.models import Course
from django.core.management.base import BaseCommand, CommandError

import requests
import json
import os
import environ  # to store env vars
env = environ.Env()
environ.Env.read_env()

class Command(BaseCommand):
    help = "Adds a user to django"

    def add_arguments(self, parser):
        parser.add_argument("school", type=str)
        parser.add_argument("term", type=str)

    def handle(self, *args, **options):
        API_URL = "https://sis.jhu.edu/api/classes"

        # check valid school
        schools = [
            "Krieger School of Arts and Sciences",
            "Whiting School of Engineering",
            # TODO: option to add support for the following schools
            # "Krieger School of Arts and Sciences Advanced Academic Programs",
            # "Nitze School of Advanced International Studies",
            # "School of Education",
            # "School of Medicine",
            # "School of Nursing",
            # "The Peabody Institute",
            # "The Peabody Preparatory",
            # "Bloomberg School of Public Health",
            # "Bloomberg School of Public Health Non-Credit",
            # "Carey Business School",
            # "Whiting School of Engineering Programs for Professionals",
        ]

        if options["school"] not in schools:
            raise CommandError("Invalid school name provided: {}".format(options["school"]))

        # check valid term
        # TODO: this could be more forgiving, allow for more terms
        terms = ["Fall 2022", "Summer 2022", "Spring 2022", "Fall 2021", "Spring 2021", "Summer 2021", "Fall 2020", "Summer 2020", "Spring 2020"]

        if options["term"] not in terms:
            raise CommandError("Invalid term provided: {}".format(options["term"]))

        # grab all courses for given school and term
        course_request = json.loads(
            requests.get(
                API_URL
                + "/"
                + options["school"].replace(" ", "%20")
                + "/"
                + options["term"].replace(" ", "%20"),
                params={"key": os.environ.get("JHU_SIS_API_TOKEN")},
            ).text
        )

        for course in course_request:
            c = json.loads(
                requests.get(
                    API_URL
                    + "/"
                    + course["OfferingName"].replace(".", "")
                    + course["SectionName"]
                    + "/"
                    + options["term"].replace(" ", "%20"),
                    params={"key": os.environ.get("JHU_SIS_API_TOKEN")},
                ).text
            )[0]

            try:
                prereq = c["SectionDetails"][0]["Prerequisites"][0]["Description"]
            except:
                prereq = ""

            try:
                coreq = c["SectionDetails"][0]["CoRequisites"][0]["Description"]
            except:
                coreq = ""

            try: 
                max_size = int(c["MaxSeats"]) 
            except ValueError:
                max_size = 0

            course_model = Course(
                name=c["Title"],
                description=c["SectionDetails"][0]["Description"],
                course_num=c["OfferingName"],
                num_credits=c["Credits"],
                department=c["Department"],
                level=c["Level"],
                prerequisites=prereq,
                corequisites=coreq,
                school=c["SchoolName"],
                campus=c["Location"],
                is_writing_intensive=(c["IsWritingIntensive"] == "Yes"),
                meeting_section=c["SectionName"],
                size=max_size,
                instructors=c["InstructorsFullName"],
                semester=(c["Term"].split(" ")[0] + " " + c["Term"].split(" ")[1]),
            )
            course_model.save()

        self.stdout.write(self.style.SUCCESS("Parsing Complete"))
