# JHcourserevU

JHcourserevU is an application to rate, review, and view reviews for the courses right here at JHU.

## User Manual

- Sign in takes the user to a Google login pop-up
- The user will enter the site at the landing page, where its functionality and purpose is introduced.
- There is a button on that landing page that, if clicked, will take the user to the list of courses they can review. There is also a button on the navigation bar at the top that will take the user to that same course display page. There are links to our GitHub page and docs, and there is a button to take the user to the list of courses they have marked as taken (if not logged in then there are no courses displayed there.)
- The dark mode button on the navigation bar (sun/moon icon) can be clicked to switch between light and dark themes for the site as a whole. This preference is saved in local storage so it persists between sessions.
- There is a search bar for the user to search courses on this course list page. They can search by course name, course number, or department.
- The course display has a pagination selector underneath the list of courses to split up the courses into manageable tile displays of 10 at a time.
- If the user prefers to view the items in vertical list format rather than tile format, there is a toggle button near the search bar.
- From the course list page, for each course tile, you can click a button to write a review or click a button to read reviews for that particular course - each of these buttons will take you to a different page for that purpose. The "Write Review" button is only visible if that courses has been marked "taken" by checking the checkbox on the course tile/list item that says "I have taken this course."
- When the above checkbox is checked, the course will also appear on the My Courses page. If the user wants to remove the course from this "taken" list, they can uncheck the checkbox and the course will no longer appear on the My Courses page.
- The review list page will display all reviews for a course, with a pagination selector underneath to split up the reviews into manageable tile displays of 10 at a time.
- There is a dropdown menu where the user can opt to only display a certain comment category (like exam style or workload.)
- In order to write a review, you will be prompted to enter the name of the professor and answer a series of guided questions about the course. When done, the user can click the submit button to post their review. A toast notification will tell the user if their review was submitted successfully (green), or if there was an error or not all fields are completed (yellow).
- At any point, if the user wants to return to the landing page, they can click the logo to take them back there.

## API Reference

# Course + Review App

The Course & Review App is allows users to access course. These courses are
directly obtained from the Johns Hopkins University [SIS Web API](https://sis.jhu.edu/api/)
and are unmodifiable. Every course can be associated with one or
more review. Every user has an associated set of courses that they
have completed, and thus, are able to review.

## API Endpoints

**WARNING**: Some HTTP responses were shortened for simplicity. Please read the
expected page limit if pagination applies to a given endpoint.

### POST /course/review/api/(int: course_id)

Generate review for a specific course.

**Example request**:

```http
GET /course/review/api/1234 HTTP/1.1
Host: https://jhcourserevu-api.herokuapp.com
Accept: application/json, text/javascript
Content-Type: application/json

{
  "course_id": 1,
  "comments": [
    "Great class",
    "Great professor",
    "Lots of work",
    "Exams were challenging"
  ]
}
```

**Example response**:

```http
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
```

- **Request Headers**

  - [Accept](https://tools.ietf.org/html/rfc7231#section-5.3.2) – the response content type depends on
    _Accept_ header

  - [Authorization](https://tools.ietf.org/html/rfc7235#section-4.2) – optional OAuth token to authenticate

- **Response Headers**

  - [Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) – this depends on _Accept_
    header of request

- **Status Codes**

  - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) – no error

  - [404 Not Found](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) – course not found

### GET /course/review/api/(int: course_id)

Obtain all reviews for a given course.

**Example request**:

```http
GET /course/review/api/1234 HTTP/1.1
Host: https://jhcourserevu-api.herokuapp.com
Accept: application/json, text/javascript
```

**Example response**:

```http
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
```

- **Query Parameters**

  - **limit** – limit number. default is 15

  - **sort** – sort by `semester` or `year`

- **Request Headers**

  - [Accept](https://tools.ietf.org/html/rfc7231#section-5.3.2) – the response content type depends on
    _Accept_ header

  - [Authorization](https://tools.ietf.org/html/rfc7235#section-4.2) – optional OAuth token to authenticate

- **Response Headers**

  - [Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) – this depends on _Accept_
    header of request

- **Status Codes**

  - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) – no error

  - [404 Not Found](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) – course or review not found

### GET /course/api

Obtain all courses with optional query parameters for
semester and year. Pagination is set by default in
increments of 10 per page.

**Example request**:

```http
GET /course/api/123 HTTP/1.1
Host: https://jhcourserevu-api.herokuapp.com
Accept: application/json, text/javascript
```

**Example response**:

```http
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
```

- **Query Parameters**

  - **page** – any integer value within range of total number of pages

  - **semester** – `spring`, `summer`, `fall`

  - **year** – any year greater than or equal to 2020

  - **limit** – limit number. default is 15

  - **sort** – sort by `semester` or `year`

- **Request Headers**

  - [Accept](https://tools.ietf.org/html/rfc7231#section-5.3.2) – the response content type depends on
    _Accept_ header

  - [Authorization](https://tools.ietf.org/html/rfc7235#section-4.2) – optional OAuth token to authenticate

- **Response Headers**

  - [Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) – this depends on _Accept_
    header of request

- **Status Codes**

  - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) – no error

  - [404 Not Found](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) – invalid semester or year

### GET /course/api/(int: course_num)

Get all courses with the given course_num with
optional query parameters for semester and year.

**Example request**:

```http
GET /course/api/EN.500.112/ HTTP/1.1
Host: https://jhcourserevu-api.herokuapp.com
Accept: application/json, text/javascript
```

**Example response**:

```http
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
```

- **Query Parameters**

  - **semester** – `spring`, `summer`, `fall`

  - **year** – any year greater than or equal to 2020

  - **limit** – limit number. default is 15

  - **sort** – sort by `semester` or `year`

- **Request Headers**

  - [Accept](https://tools.ietf.org/html/rfc7231#section-5.3.2) – the response content type depends on
    _Accept_ header

  - [Authorization](https://tools.ietf.org/html/rfc7235#section-4.2) – optional OAuth token to authenticate

- **Response Headers**

  - [Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) – this depends on _Accept_
    header of request

- **Status Codes**

  - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) – no error

  - [404 Not Found](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) – invalid semester or year

## About Us!

- Bridget Carr
- Sebastian Cabrejos
- Melody Hsu
- Tsige Solomon
- Narayani Wagle
- Stephania Rincon Godinez
- Theodore Xie
