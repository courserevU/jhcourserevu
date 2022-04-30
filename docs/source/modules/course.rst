Course + Review App
###########################

The Course & Review App is allows users to access course. These courses are
directly obtained from the Johns Hopkins University `SIS Web API <https://sis.jhu.edu/api/>`_
and are unmodifiable. Every course can be associated with one or
more review. Every user has an associated set of courses that they
have completed, and thus, are able to review.

API Endpoints
*************

.. warning::
  Some HTTP responses were shortened for simplicity. Please read the
  expected page limit if pagination applies to a given endpoint.

.. http:post:: /course/review/api/(int: course_id)

   Generate review for a specific course.

   **Example request**:

   .. sourcecode:: http

      GET /course/review/api/1234 HTTP/1.1
      Host: https://jhcourserevu-api.herokuapp.com
      Accept: application/json, text/javascript
      Content-Type: application/json

      {
        "comments": {
          "Professor": "Dr. Ali Madooei",
          "Teaching Style": "FUN",
          "Grading Style": "CHILL",
          "Teacher Feedback": "NICE JOB",
          "Workload": "LIGHT",
          "Assignment Style": "projects",
          "Exam Style": "stylized"
        },
        "course_id": 1
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": 1,
        "comments": [
          "Great class", 
          "Great professor", 
          "Lots of work",
          "Exams were challenging"
        ]
      }

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: course not found

.. http:get:: /course/review/api/(int: course_id)

   Obtain all reviews for a given course.

   **Example request**:

   .. sourcecode:: http

      GET /course/review/api/1234 HTTP/1.1
      Host: https://jhcourserevu-api.herokuapp.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      [
        {
          "id": 1,
          "course_id": 1234,
          "comments": [
            "Great class", 
            "Great professor", 
            "Lots of work",
            "Exams were challenging"
          ]
        },
        {
          "id": 2,
          "course_id": 1234,
          "comments": [
            "Okay class", 
            "Okay professor", 
            "Work was... okay",
            "Exams were also... okay"
          ]
        }
      ]

   :query limit: limit number, default is 10
   :query sort: sort by ``semester`` or ``year``

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: course or review not found

.. http:get:: /course/api

   Obtain all courses with optional query parameters for
   semester and year. Pagination is set by default in 
   increments of 10 per page.

   **Example request**:

   .. sourcecode:: http

      GET /course/api/123 HTTP/1.1
      Host: https://jhcourserevu-api.herokuapp.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "count": 2312,
        "next": "http://jhcourserevu-api.herokuapp.com/course/api/?page=2",
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "Gateway Computing: JAVA",
                "description": "This course introduces fundamental programming concepts and techniques, and is intended for all who plan to develop computational artifacts or intelligently deploy computational tools in their studies and careers. Topics covered include the design and implementation of algorithms using variables, control structures, arrays, functions, files, testing, debugging, and structured program design. Elements of object-oriented programming. algorithmic efficiency and data visualization are also introduced. Students deploy programming to develop working solutions that address problems in engineering, science and other areas of contemporary interest that vary from section to section. Course homework involves significant programming. Attendance and participation in class sessions are expected.",
                "course_num": "EN.500.112",
                "num_credits": "3.00",
                "department": "EN General Engineering",
                "level": "Lower Level Undergraduate",
                "prerequisites": "Students may not have earned credit in courses:  EN.500.113 OR EN.500.114 OR EN.510.202 OR EN.530.112 OR EN.580.200 OR EN.601.107 OR EN.500.132 OR EN.500.133 OR EN.500.134.",
                "corequisites": "",
                "school": "Whiting School of Engineering",
                "campus": "Homewood Campus",
                "is_writing_intensive": "False",
                "meeting_section": "01",
                "size": 19,
                "instructors": "Staff",
                "semester": "Spring 2022"
            },
            {
                "id": 2,
                "name": "Gateway Computing: JAVA",
                "description": "This course introduces fundamental programming concepts and techniques, and is intended for all who plan to develop computational artifacts or intelligently deploy computational tools in their studies and careers. Topics covered include the design and implementation of algorithms using variables, control structures, arrays, functions, files, testing, debugging, and structured program design. Elements of object-oriented programming. algorithmic efficiency and data visualization are also introduced. Students deploy programming to develop working solutions that address problems in engineering, science and other areas of contemporary interest that vary from section to section. Course homework involves significant programming. Attendance and participation in class sessions are expected.",
                "course_num": "EN.500.112",
                "num_credits": "3.00",
                "department": "EN General Engineering",
                "level": "Lower Level Undergraduate",
                "prerequisites": "Students may not have earned credit in courses:  EN.500.113 OR EN.500.114 OR EN.510.202 OR EN.530.112 OR EN.580.200 OR EN.601.107 OR EN.500.132 OR EN.500.133 OR EN.500.134.",
                "corequisites": "",
                "school": "Whiting School of Engineering",
                "campus": "Homewood Campus",
                "is_writing_intensive": "False",
                "meeting_section": "02",
                "size": 19,
                "instructors": "Darvish Darab, Mohammad Ali",
                "semester": "Spring 2022"
            }
        ]
      }

   :query page: any integer value within range of total number of pages
   :query semester: ``spring``, ``summer``, ``fall``
   :query year: any year greater than or equal to 2020
   :query limit: limit number, default is 10
   :query sort: sort by ``semester`` or ``year``

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: invalid semester or year

.. http:get:: /course/api/(int: course_num)

   Get all courses with the given course_num with 
   optional query parameters for semester and year.

   **Example request**:

   .. sourcecode:: http

      GET /course/api/EN.500.112/ HTTP/1.1
      Host: https://jhcourserevu-api.herokuapp.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      [
        {
            "id": 1,
            "name": "Gateway Computing: JAVA",
            "description": "This course introduces fundamental programming concepts and techniques, and is intended for all who plan to develop computational artifacts or intelligently deploy computational tools in their studies and careers. Topics covered include the design and implementation of algorithms using variables, control structures, arrays, functions, files, testing, debugging, and structured program design. Elements of object-oriented programming. algorithmic efficiency and data visualization are also introduced. Students deploy programming to develop working solutions that address problems in engineering, science and other areas of contemporary interest that vary from section to section. Course homework involves significant programming. Attendance and participation in class sessions are expected.",
            "course_num": "EN.500.112",
            "num_credits": "3.00",
            "department": "EN General Engineering",
            "level": "Lower Level Undergraduate",
            "prerequisites": "Students may not have earned credit in courses:  EN.500.113 OR EN.500.114 OR EN.510.202 OR EN.530.112 OR EN.580.200 OR EN.601.107 OR EN.500.132 OR EN.500.133 OR EN.500.134.",
            "corequisites": "",
            "school": "Whiting School of Engineering",
            "campus": "Homewood Campus",
            "is_writing_intensive": "False",
            "meeting_section": "01",
            "size": 19,
            "instructors": "Staff",
            "semester": "Spring 2022"
        },
        {
            "id": 2,
            "name": "Gateway Computing: JAVA",
            "description": "This course introduces fundamental programming concepts and techniques, and is intended for all who plan to develop computational artifacts or intelligently deploy computational tools in their studies and careers. Topics covered include the design and implementation of algorithms using variables, control structures, arrays, functions, files, testing, debugging, and structured program design. Elements of object-oriented programming. algorithmic efficiency and data visualization are also introduced. Students deploy programming to develop working solutions that address problems in engineering, science and other areas of contemporary interest that vary from section to section. Course homework involves significant programming. Attendance and participation in class sessions are expected.",
            "course_num": "EN.500.112",
            "num_credits": "3.00",
            "department": "EN General Engineering",
            "level": "Lower Level Undergraduate",
            "prerequisites": "Students may not have earned credit in courses:  EN.500.113 OR EN.500.114 OR EN.510.202 OR EN.530.112 OR EN.580.200 OR EN.601.107 OR EN.500.132 OR EN.500.133 OR EN.500.134.",
            "corequisites": "",
            "school": "Whiting School of Engineering",
            "campus": "Homewood Campus",
            "is_writing_intensive": "False",
            "meeting_section": "02",
            "size": 19,
            "instructors": "Darvish Darab, Mohammad Ali",
            "semester": "Spring 2022"
        }
      ]

   :query semester: ``spring``, ``summer``, ``fall``
   :query year: any year greater than or equal to 2020
   :query limit: limit number, default is 10
   :query sort: sort by ``semester`` or ``year``

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: invalid semester or year

Models
**************
.. automodule:: course.models
    :members:

Views
**************
.. automodule:: course.views
    :members:

Serializers
**************
.. automodule:: course.api.serializers
    :members:

