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
- [User Manual](https://cs421sp22-homework.github.io/project-team-08-random/)
- [API Documentation](https://cs421sp22-homework.github.io/project-team-08-random/)

## Installing / Getting started

### Backend (Django)

Before anything else, enter the backend dir:
```shell
cd code/backend
```
There are a few options here to activate the backend:
### Docker (Recommended)
Install [Docker](https://www.docker.com/products/docker-desktop/).
Make sure you open Docker before starting!
```
docker compose up
```

### Python Virtual Environment
```
python3 -m venv django-venv # Assumes you have Python3 installed

source django-venv/bin/activate

pip3 install -r requirements.txt

python manage.py runserver

# Use command: CTRL-C to exit

deactivate
```

Regardless of which method you used, you can then head to `http://0.0.0.0:8000/` and
get started with developing!

### Frontend (Vue)

```shell
cd code/frontend

npm install # Assumes you have npm installed

npm run dev
```

## Developing

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
