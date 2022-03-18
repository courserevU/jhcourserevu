User App
#########

The user app is allows users to sign up and log in. Every user is 
view anonymously to the general public. Every user has an associated
JHED ID and email to sign up or login.

API Endpoints
**************

.. http:post:: /user/api/signup
    
    Generate new user

   **Example request**:

   .. sourcecode:: http

      GET /user/api/123 HTTP/1.1
      Host: https://jhcourserevu-api.herokuapp.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      [
        {
          "user_id": 1,
          "jhed_id": "scabrej1",
          "jhed_email": "scabrej1@jhu.edu",
        }
      ]

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: unable to validate credentials

.. http:get:: /user/api/(int: user_id)
    
    Get a user by id.

   **Example request**:

   .. sourcecode:: http

      GET /user/api/123 HTTP/1.1
      Host: https://jhcourserevu-api.herokuapp.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      [
        {
          "user_id": 1,
          "jhed_id": "scabrej1",
          "jhed_email": "scabrej1@jhu.edu",
        }
      ]

   :query courses: courses completed by user
   :query name: name of User
   :query jhed: JHED ID of User
   :query jhed_email: JHED email of User

   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: user not found

Models
~~~~~~
.. automodule:: user.models
    :members:

Views
~~~~~
.. automodule:: user.views
    :members:

Serializers
~~~~~~~~~~~
.. automodule:: user.api.serializers
    :members:
