from course.models import Course
from django.core.management.base import BaseCommand, CommandError

import requests
import json

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("school", type=str)
# parser.add_argument("term", type=str)
# args = parser.parse_args()


class Command(BaseCommand):
    help = "Adds a user to django"

    def add_arguments(self, parser):
        parser.add_argument("school", type=str)
        parser.add_argument("term", type=str)

    def handle(self, *args, **options):
        API_URL = "https://sis.jhu.edu/api/classes"

        # check valid school
        schools = [
            # "Bloomberg School of Public Health",
            # "Bloomberg School of Public Health Non-Credit",
            # "Carey Business School",
            "Krieger School of Arts and Sciences",
            # "Krieger School of Arts and Sciences Advanced Academic Programs",
            # "Nitze School of Advanced International Studies",
            # "School of Education",
            # "School of Medicine",
            # "School of Nursing",
            # "The Peabody Institute",
            # "The Peabody Preparatory",
            "Whiting School of Engineering",
            # "Whiting School of Engineering Programs for Professionals",
        ]

        if options["school"] not in schools:
            raise CommandError("Invalid school name provided: %s" % options["school"])

        # check valid term
        terms = ["Fall 2022", "Summer 2022", "Spring 2022"]

        if options["term"] not in terms:
            raise CommandError("Invalid term provided: %s" % options["term"])

        # grab all courses for given school and term
        course_request = json.loads(
            requests.get(
                API_URL
                + "/"
                + options["school"].replace(" ", "%20")
                + "/"
                + options["term"].replace(" ", "%20"),
                params={"key": "rZW4VwAUE1WTYZfSZyldykJLOXUC59fr"},
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
                    params={"key": "rZW4VwAUE1WTYZfSZyldykJLOXUC59fr"},
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
                size=(isinstance(c["MaxSeats"], int) if c["MaxSeats"] else 0),
                instructors=c["InstructorsFullName"],
                semester=(c["Term"].split(" ")[0] + " " + c["Term"].split(" ")[1]),
            )
            course_model.save()

        self.stdout.write(self.style.SUCCESS("Parsing Complete"))
