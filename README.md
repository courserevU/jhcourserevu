# JHcourserevU

JHcourserevU is an application to rate, review, and view reviews for the courses right here at JHU.

**Team**

| Name                     | JHU Email        | GitHub Username |
| ------------------------ | ---------------- | --------------- |
| Bridget Carr             | bcarr15@jhu.edu  | bcarr15         |
| Sebastian Cabrejos       | scabrej1@jhu.edu | boccca2014      |
| Stephania Rincon Godinez | srincon3@jhu.edu | Stephrg         |
| Tsige Solomon            | tsolomo8@jhu.edu | tsigeas         |
| Melody Hsu               | mhsu13@jhu.edu   | melodymhsu      |
| Narayani Wagle           | nwagle1@jhu.edu  | nhwagle         |
| Theodore Xie             | txie10@jhu.edu   | theodore-xie    |

**Advisors**

| Name       | JHU Email       | GitHub Username |
| ---------- | --------------- | --------------- |
| Melody Lee | hlee244@jhu.edu | melodyhplee     |

# Documentation

- [Project Document](https://docs.google.com/document/d/1ERXfE-sJ2X_Asr5cXk-hHA5Ayl_FxULpkI7nzGDUnOM)
- [User Manual](https://cs421sp22-homework.github.io/project-team-08-random/)
- [API Documentation](https://cs421sp22-homework.github.io/project-team-08-random/)

# Installing / Getting started

We recommend forking the repository before starting, so you can maintain
your own instance of the application.

## Backend (Django)

Before anything else, enter the backend directory:

```shell
cd code/backend
```

There are a **two** options here to activate the backend:

### Docker (Recommended)

1. Install [Docker](https://www.docker.com/products/docker-desktop/).
2. Make sure you open Docker before starting!
3.

```shell
docker compose up
```

4. Head to [http://0.0.0.0:8000/](http://0.0.0.0:8000/) and get started with developing!

EXITING

5. Use CTRL-C to stop the docker container.

### Python Virtual Environment

1. Create the Python Virtual Environment

```shell
python3 -m venv django-venv # Assumes you have Python3 installed
```

2. Enter the environment (Make sure to setup your Python Virtual environment
   as "django-venv" to avoid pushing it to your remote repository!)

```
source django-venv/bin/activate
```

3. Install the requirements

```shell
pip3 install -r requirements.txt
```

4. Run the Server!

```shell
python manage.py runserver
```

5. Head to [http://0.0.0.0:8000/](http://0.0.0.0:8000/) and start developing!

EXITING

6. Use CTRL-C to stop program.

7. Exit the Python Virtual Environment.

```shell
deactivate
```

# Frontend Local Development (Vue)

1. Enter the directory.

```shell
cd code/frontend
```

2. Install all dependencies.

```shell
npm install # Assumes you have npm installed
```

3. Run the frontend development view.

```shell
npm run dev
```

# Setting up Your Environment Variables

In order to use our application locally, you need to
set up the environment variables (i.e. secrets, token, etc.)
to get data from the other platforms this product relies on.

Please head to `code/backend/jhcourserevu` and create a file
called `.env`. Refer to `.env.example` to see how your original
`.env` file should look like. Likewise, for the frontend, you must
create both `.env` and `.env.production` file matching the credentials
in the `.env.example` file.

# Populating the Database

In order to populate your local database, we need to
get data from the [SIS Web API](https://sis.jhu.edu/api/).

If you head to `code/backend/management/commands`, you will
find the file `course_parser.py`. It does the following to populate
your database with courses.

1. Sends a **HTTP GET request** to the SIS Web API.

2. Converts the data readable by Django using the respective **Serializer** for course.

3. Stores the new objects into the Postgres database.

You can run the following command inside your **Docker** shell or
inside `code/backend` if you’re using the **Python Virtual Environment**.

```shell
python manage.py course_parser [SCHOOL_NAME] [SEMESTER YEAR]
```

Here’s one example. You can get data for the **Whiting School of Engineering** in **Fall 2022**.

```shell
python manage.py course_parser "Whiting School of Engineering" "Fall 2022"
```

Here’s a list of all possible schools:

- Krieger School of Arts and Sciences

- Whiting School of Engineering

And the current semester and all previous semesters where there is
data (currently from 2009 & thereafter):

- Fall 2022

- Spring 2022

- Fall 2021

and so on.

# Deployment

There are many different options deploy this application.
We opted to use [Netlify](https://www.netlify.com/)
for Frontend deployment and [Heroku](https://www.heroku.com/)
for Backend deployment.

## VueJS Frontend - Netlify

You can refer to the directory `.github/workflows`. The
files `frontend_stage.yml` (for staging/development) and
`frontend.yml` (for production). If you choose to setup
your own version, you must fill in the relevant environment
variables in GitHub.

It is necessary to create a `.env.production` and `.env` file in
the `code/frontend` folder with the relevant fields following the
layout of `.env.example`.

## Django Web Server - Heroku

You can refer to the directory `.github/workflows`. The
files `backend.yml` (for staging/development & production).
If you choose to setup your own version, you must fill in the
relevant environment variables in Heroku.

It is necessary to create a `.env` file in the
`code/backend/jhcourserevu` folder with the relevant fields
following the layout of `.env.example`.

# Login Flow

This is multi-step process. The most accurate depiction of
the login flow can best depicted by the following graphic:

![image](/docs/files/vue3_login-flow.png)

Credit: [vue3-google-oauth2](https://github.com/guruahn/vue3-google-oauth2)

## OAuth2 for Frontend (vue3-google-oauth2)

To get the Google Login Prompt and parse the information from the user,
this app uses [vue3-google-oauth2](https://github.com/guruahn/vue3-google-oauth2).

## OAuth2 for Backend (drf-rest-oauth2)

To create a CustomUser in the Postgres Database, the frontend makes a
call to the backend’s Restful API. The app uses
[drf-rest-oauth2](https://github.com/wagnerdelima/drf-social-oauth2) to
obtain a User Access Token and gather the user’s information and store it
accordingly.

<!--
You should include what is needed (e.g. all of the configurations) to set up the dev environment. For instance, global dependencies or any other tools (include download links), explaining what database (and version) has been used, etc. If there is any virtual environment, local server, ..., explain here.

Additionally, describe and show how to run the tests, explain your code style and show how to check it.

If your project needs some additional steps for the developer to build the project after some code changes, state them here. Moreover, give instructions on how to build and release a new version. In case there's some step you have to take that publishes this project to a server, it must be stated here. -->
