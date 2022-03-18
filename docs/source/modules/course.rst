Course + Review App
###########################

The Course & Review App is allows users to access course. These courses are
directly obtained from the Johns Hopkins University `SIS Web API <https://sis.jhu.edu/api/>`_
and are unmodifiable. Every course can be associated with one or
more review. Every user has an associated set of courses that they
have completed, and thus, are able to review.

API Endpoints
*************

.. http:post:: /course/review/api/(int: course_id)

   Generate review for a specific course.

   **Example request**:

   .. sourcecode:: http

      GET /course/review/api/123 HTTP/1.1
      Host: https://jhcourserevu-api.herokuapp.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      [
        {
          "review_id": 1,
          "author_id": 123,
          "comments": [
            "Great class", 
            "Great professor", 
            "Lots of work",
            "Exams were challenging"
          ],
        },
      ]

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: course not found

.. http:get:: /course/review/api/(int: course_id)

   Obtain reviews for a given course.

   **Example request**:

   .. sourcecode:: http

      GET /course/review/api/123 HTTP/1.1
      Host: https://jhcourserevu-api.herokuapp.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      [
        {
          "review_id": 1,
          "author_id": 123,
          "comments": [
            "Great class", 
            "Great professor", 
            "Lots of work",
            "Exams were challenging"
          ],
        },
        {
          "review_id": 2,
          "author_id": 123,
          "comments": [
            "Great class", 
            "Great professor", 
            "Lots of work",
            "Exams were challenging"
          ],
        }
      ]

   :query review_id: The id of the review to retrieve.
   :query limit: limit number. default is 15
   :query sort: sort by ``semester`` or ``year``

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: course or review not found

.. http:get:: /course/api

   Obtain all courses with optional query parameters for
   semester and year.

   **Example request**:

   .. sourcecode:: http

      GET /course/review/123 HTTP/1.1
      Host: https://jhcourserevu-api.herokuapp.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      [
        {
          "course_id": 12346,
          "name": ,
          "description": ,
          "department": ,
          "number": ,
          "section": ,
          "semester": ,
          "year": ,
          "instructor": ,
        },
      ]

   :query semester: ``spring``, ``summer``, ``fall``
   :query year: any year greater than or equal to 2020
   :query limit: limit number. default is 15
   :query sort: sort by ``semester`` or ``year``

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: invalid semester or year

Models
~~~~~~
.. automodule:: course.models
    :members:

Views
~~~~~
.. automodule:: course.views
    :members:

Serializers
~~~~~~~~~~~
.. automodule:: course.api.serializers
    :members:

