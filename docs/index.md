# JHcourserevU

JHcourserevU is an application to rate, review, and view reviews for the courses right here at JHU.

## User Manual

* The user will enter the site at the landing page, where its functionality and purpose is introduced
* There is a button on that landing page that, if clicked, will take the user to the list of courses they can review. There is also a button on the navigation bar at the top that will take the user to the course display page.
* The dark mode button on the navigation bar (sun/moon icon) can be clicked to switch between light and dark themes for the site as a whole. This preference is saved in local storage so it persists between sessions.
* There is a search bar for the user to search courses on this course list page. They can search by course name or course number.
* The course display has a pagination selector underneath the list of courses to split up the courses into manageable tile displays.
* From the course list page, for each course tile, you can click a button to write a review or click a button to read reviews for that particular course - each of these buttons will take you to a different page for that purpose.
* The review list page will display all reviews for a course, with a pagination selector underneath to split up the reviews into manageable tile displays.
* In order to write a review, you will be prompted to enter the name of the professor, pick a semester from a dropdown menu, and answer a series of guided questions about the course. When done, the user can click the submit button to post their review.
* At any point, if the user wants to return to the landing page, they can click the logo to take them back there.
* The sign-in and sign-up buttons on the navigation bar take the user to login and registration pages respectively, where the user can enter an email and password and then click the button underneath to submit their account information.


## API Reference

# Course + Review App

The Course & Review App is allows users to access course. These courses are
directly obtained from the Johns Hopkins University [SIS Web API](https://sis.jhu.edu/api/)
and are unmodifiable. Every course can be associated with one or
more review. Every user has an associated set of courses that they
have completed, and thus, are able to review.

## API Endpoints


### POST /course/review/api/(int: course_id)
Generate review for a specific course.

**Example request**:

```http
GET /course/review/api/123 HTTP/1.1
Host: https://jhcourserevu.herokuapp.com
Accept: application/json, text/javascript
```

**Example response**:

```http
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
```


* **Request Headers**

    
    * [Accept](https://tools.ietf.org/html/rfc7231#section-5.3.2) – the response content type depends on
    *Accept* header


    * [Authorization](https://tools.ietf.org/html/rfc7235#section-4.2) – optional OAuth token to authenticate



* **Response Headers**

    
    * [Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) – this depends on *Accept*
    header of request



* **Status Codes**

    
    * [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) – no error


    * [404 Not Found](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) – course not found



### GET /course/review/api/(int: course_id)
Obtain reviews for a given course.

**Example request**:

```http
GET /course/review/api/123 HTTP/1.1
Host: https://jhcourserevu.herokuapp.com
Accept: application/json, text/javascript
```

**Example response**:

```http
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
```


* **Query Parameters**

    
    * **review_id** – The id of the review to retrieve.


    * **limit** – limit number. default is 15


    * **sort** – sort by `semester` or `year`



* **Request Headers**

    
    * [Accept](https://tools.ietf.org/html/rfc7231#section-5.3.2) – the response content type depends on
    *Accept* header


    * [Authorization](https://tools.ietf.org/html/rfc7235#section-4.2) – optional OAuth token to authenticate



* **Response Headers**

    
    * [Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) – this depends on *Accept*
    header of request



* **Status Codes**

    
    * [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) – no error


    * [404 Not Found](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) – course or review not found



### GET /course/api
Obtain all courses with optional query parameters for
semester and year.

**Example request**:

```http
GET /course/review/123 HTTP/1.1
Host: https://jhcourserevu.herokuapp.com
Accept: application/json, text/javascript
```

**Example response**:

```http
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
```


* **Query Parameters**

    
    * **semester** – `spring`, `summer`, `fall`


    * **year** – any year greater than or equal to 2020


    * **limit** – limit number. default is 15


    * **sort** – sort by `semester` or `year`



* **Request Headers**

    
    * [Accept](https://tools.ietf.org/html/rfc7231#section-5.3.2) – the response content type depends on
    *Accept* header


    * [Authorization](https://tools.ietf.org/html/rfc7235#section-4.2) – optional OAuth token to authenticate



* **Response Headers**

    
    * [Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) – this depends on *Accept*
    header of request



* **Status Codes**

    
    * [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) – no error


    * [404 Not Found](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) – invalid semester or year


# User App

The user app is allows users to sign up and log in. Every user is
view anonymously to the general public. Every user has an associated
JHED ID and email to sign up or login.

## API Endpoints

### POST /user/api/signup
> Generate new user

**Example request**:

```http
GET /user/api/123 HTTP/1.1
Host: https://jhcourserevu.herokuapp.com
Accept: application/json, text/javascript
```

**Example response**:

```http
HTTP/1.1 200 OK
Vary: Accept
Content-Type: text/javascript

[
  {
    "user_id": 1,
    "jhed_id": "scabrej1",
    "jhed_email": "scabrej1@jhu.edu",
    "preferred_name": "Sebastian",
    "is_admin": false,
  }
]
```


* **Request Headers**

    
    * [Accept](https://tools.ietf.org/html/rfc7231#section-5.3.2) – the response content type depends on
    *Accept* header


    * [Authorization](https://tools.ietf.org/html/rfc7235#section-4.2) – optional OAuth token to authenticate



* **Response Headers**

    
    * [Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) – this depends on *Accept*
    header of request



* **Status Codes**

    
    * [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) – no error


    * [404 Not Found](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) – unable to validate credentials



### GET /user/api/login
> Get a user by id.

**Example request**:

```http
GET /user/api/123 HTTP/1.1
Host: https://jhcourserevu.herokuapp.com
Accept: application/json, text/javascript
```

**Example response**:

```http
HTTP/1.1 200 OK
Vary: Accept
Content-Type: text/javascript

[
  {
    "user_id": 1,
    "jhed_id": "scabrej1",
    "jhed_email": "scabrej1@jhu.edu",
    "preferred_name": "Sebastian",
    "is_admin": false,
  }
]
```


* **Query Parameters**

    
    * **courses** – courses completed by user


    * **name** – name of User


    * **jhed** – JHED ID of User


    * **jhed_email** – JHED email of User



* **Request Headers**

    
    * [Accept](https://tools.ietf.org/html/rfc7231#section-5.3.2) – the response content type depends on
    *Accept* header


    * [Authorization](https://tools.ietf.org/html/rfc7235#section-4.2) – optional OAuth token to authenticate



* **Response Headers**

    
    * [Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) – this depends on *Accept*
    header of request



* **Status Codes**

    
    * [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) – no error


    * [404 Not Found](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) – user not found



## About Us!

- Bridget Carr
- Sebastian Cabrejos
- Melody Hsu
- Tsige Solomon
- Narayani Wagle
- Stephania Rincon Godinez
- Theodore Xie
