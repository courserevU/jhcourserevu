Login Flow
############

This is multi-step process. The most accurate depiction of
the login flow can best depicted by the following graphic.
.. image::files/vue3_login-flow.png
    :width: 400
    :alt: Login Flow Diagram

OAuth2 for Frontend (vue3-google-oauth2)
*****************************************

To get the Google Login Prompt and parse the information from the user, 
this app uses `vue3-google-oauth2 <https://github.com/guruahn/vue3-google-oauth2>`_.

OAuth2 for Backend (drf-rest-oauth2)
*************************************

To create a `CustomUser` in the Postgres Database, the frontend makes a
call to the backend's Restful API. The app uses
`drf-rest-oauth2 <https://github.com/wagnerdelima/drf-social-oauth2>`_ to
use the User Access Token to gather the user's information and store it
accordingly.
