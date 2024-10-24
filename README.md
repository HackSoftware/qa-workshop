# QA Workshop Sample Project

This is just a simple Django admin made for automation test purposes. 

## How to start the project locally

```
docker compose build
docker compose run web python manage.py migrate
docker compose up
```

## How to create a user

```
docker compose run web python manage.py createsuperuser
```

## How to flush the database
```
docker compose run web python manage.py flush
```