# django_simple_chatbot

Simple chatbot written with Django rest framework and React, which can communicate using the preloaded dialogs (questionnaires).

This repo contains frontend and backend applications and docker-compose file for running them.

## Running

1. `docker-compose build`
1. `docker-compose up`
1. After running apps you can access them by urls:
  - [http://127.0.0.1:8000](http://127.0.0.1:5000) is backend app written with Django rest framework
  - [http://127.0.0.1:3000](http://127.0.0.1:3000) is frontend app written with React

Before using the application, you need to load the JSON questionnaires through the Upload in web browsable API.
