Deployment
############

There are many different options deploy this application, 
but we opted to use `Netlify <https://www.netlify.com/>`_ 
for Frontend deployment and `Heroku <https://www.heroku.com/>`_
for Backend deployment.

VueJS Frontend - Netlify
**************************
You can refer to the directory `.github/workflows`. The
files `frontend_stage.yml` (for staging/development) and 
`frontend.yml` (for production). If you choose to setup
your own version, you must fill in the relevant environment
variables in GitHub.

It is necessary to create a `.env.production` file in the
`code/frontend` folder with the relevant fields following the
layout of `.env.example`.

Django Web Server - Heroku
****************************
You can refer to the directory `.github/workflows`. The
files `backend.yml` (for staging/development & production). 
If you choose to setup your own version, you must fill in the 
relevant environment variables in Heroku.

It is necessary to create a `.env` file in the
`code/backend/jhcourserevu` folder with the relevant fields 
following the layout of `.env.example`.
