User App
#########

The user app is allows users to sign up and log in. Every user is 
view anonymously to the general public. Every user has an associated
Google Account.

API Endpoints
**************

.. http:post:: /auth/convert-token
    
   Create new user using Google OAuth2.0 credentials. 
   Utilized by `drf-rest-oauth2 <https://github.com/wagnerdelima/drf-social-oauth2>`_.

   **Example request**:

   .. sourcecode:: http

      GET /auth/convert-token HTTP/1.1
      Host: https://jhcourserevu-api-test.herokuapp.com
      Accept: application/json, text/javascript

      {
         grant_type: "convert_token",
         client_id: DJANGO_CLIENT_ID,
         client_secret: DJANGO_CLIENT_SECRET,
         backend: "google-oauth2",
         token: access_token,
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      {
         "access_token" : alphanumeric
      }

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: unable to validate credentials

.. http:get:: /user/api/(int: user_email)
    
    Get a user_id by email.

   **Example request**:

   .. sourcecode:: http

      GET /user/api/random123@test.email HTTP/1.1
      Host: https://jhcourserevu-api.herokuapp.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      {
         "id": 1,
      }

   :query id: user id

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: user not found

.. http:get:: /user/api/id/(int: user_id)
    
    Get a user's courses by user_id.

   **Example request**:

   .. sourcecode:: http

      GET /user/api/id/0 HTTP/1.1
      Host: https://jhcourserevu-api.herokuapp.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      {
         "count": 2,
         "next": null,
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

   :query limit: limit number, default is 10
   :query count: number of courses for user

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: user not found

.. http:post:: /user/api/
    
   Add course to user's set of "my courses"

   **Example request**:

   .. sourcecode:: http

      GET /user/api/ HTTP/1.1
      Host: https://jhcourserevu-api.herokuapp.com
      Accept: application/json, text/javascript

      Content-Type: application/json

      {
        "user_id": 1,
        "course_id": 1,
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      {
         "id": 11,
         "user": 5,
         "courses": [
            1
         ]
      }

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: unable to validate credentials

.. http:delete:: /user/api/
    
   Remove course to user's set of "my courses"

   **Example request**:

   .. sourcecode:: http

      GET /user/api/ HTTP/1.1
      Host: https://jhcourserevu-api.herokuapp.com
      Accept: application/json, text/javascript

      Content-Type: application/json

      {
        "user_id": 1,
        "course_id": 1,
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 OK
      Vary: Accept
      Content-Type: text/javascript

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 204: no content/error
   :statuscode 404: unable to validate credentials

Models
**************
.. automodule:: user.models
    :members:

Views
**************
.. automodule:: user.views
    :members:

Serializers
**************
.. automodule:: user.api.serializers
    :members:
