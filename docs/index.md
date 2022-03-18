# JHcourserevU

JHcourserevU is an application to rate, review, and view reviews for the courses right here at JHU.

## User Manual

Documentation for your users on how to use the app! 

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
Host: https://jhcourserevu-api.herokuapp.com
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
Host: https://jhcourserevu-api.herokuapp.com
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
Host: https://jhcourserevu-api.herokuapp.com
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
Host: https://jhcourserevu-api.herokuapp.com
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
Host: https://jhcourserevu-api.herokuapp.com
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