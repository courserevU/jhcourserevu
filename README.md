# JHcourserevU

JHcourserevU is an application to rate, review, and view reviews for the courses right here at JHU.

**Team**

| Name                     | JHU Email        | GitHub Username |
| ------------------------ | ---------------- | --------------- |
| Theodore Xie             | txie10@jhu.edu   | theodore-xie    |
| Sebastian Cabrejos       | scabrej1@jhu.edu | boccca2014      |
| Melody Hsu               | mhsu13@jhu.edu   | melodymhsu      |
| Bridget Carr             | bcarr15@jhu.edu  | bcarr15         |
| Tsige Solomon            | tsolomo8@jhu.edu | tsigeas         |
| Narayani Wagle           | nwagle1@jhu.edu  | nhwagle         |
| Stephania Rincon Godinez | srincon3@jhu.edu | Stephrg         |

**Advisors**

| Name       | JHU Email       | GitHub Username |
| ---------- | --------------- | --------------- |
| Melody Lee | hlee244@jhu.edu | melodyhplee     |

## Documentation

- [Project Document](https://docs.google.com/document/d/1ERXfE-sJ2X_Asr5cXk-hHA5Ayl_FxULpkI7nzGDUnOM)
- [User Manual](link/to/GitHubPage)
- [API Documentation](link/to/GitHubPage/api)

## Installing / Getting started

A quick introduction of the minimal setup you need to get the app up & running on a local computer. For example, your advisor might use the instruction here to run the application locally.

### Backend (Django)

```shell
cd code/backend

python3 -m venv django-venv # Assumes you have Python3 installed

source django-venv/bin/activate

pip3 install -r requirements.txt

python manage.py runserver

# Use command: CTRL-C to exit

deactivate
```

### Frontend (Vue)

```shell
cd code/frontend

npm install # Assumes you have npm installed

npm run dev
```

## Developing
<!-- Detailed and step-by-step documentation for setting up local development. For example, a new team member will use these instructions to start developing the project further. -->

Begin with the same commands as the previous section for frontend and backend, respectively
### Backend
Make sure to setup your Python Virtual environment
as "django-venv" to avoid pushing it to the remote repository.

<!-- ```shell

``` -->

<!-- 
You should include what is needed (e.g. all of the configurations) to set up the dev environment. For instance, global dependencies or any other tools (include download links), explaining what database (and version) has been used, etc. If there is any virtual environment, local server, ..., explain here.

Additionally, describe and show how to run the tests, explain your code style and show how to check it.

If your project needs some additional steps for the developer to build the project after some code changes, state them here. Moreover, give instructions on how to build and release a new version. In case there's some step you have to take that publishes this project to a server, it must be stated here. -->

Will add Django API documentation via SwaggerUI and/or ReDoc.
