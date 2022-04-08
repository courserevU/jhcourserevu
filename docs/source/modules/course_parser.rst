Populating the Database
###########################

In order to populate your local database, we need to
get data from the `SIS Web API <https://sis.jhu.edu/api/>`_. 

If you head to ``code/backend/management/commands``, you will
find the file ``course_parser.py``. It does the following to populate
your database with courses.

#. Sends a ``HTTP GET request`` to the SIS Web API. 
#. Converts the data readable by Django using the respective ``Serializer`` for course.
#. Stores the  new objects into the Postgres database.

You can run the following command inside your ``Docker`` shell or
inside ``code/backend`` if you're using the ``Python Virtual Environment``.

.. code-block:: shell

    python manage.py course_parser [SCHOOL_NAME] [SEMESTER YEAR]

Here's one example. You can get data for the Whiting School of Engineering in Fall 2022.

.. code-block:: shell

    python manage.py course_parser "Whiting School of Engineering" "Fall 2022"

Here's a list of all possible schools:

* Krieger School of Arts and Sciences
* Whiting School of Engineering

And the current semester and all previous semesters where there is
data (currently all the way back to 2009):

* Fall 2022
* Spring 2022
* Fall 2021

and so on.