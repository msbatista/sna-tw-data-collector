# sna-tw-data-collector

## Introduction
A very simple wrapper around `Tweepy` to track twitter data and insert into a mongodb collection.

## Instalation
```
python3 -m venv .venv
source .venv/bin/activate
make setup
```
Replace the environment variables in the generated `.env file. 
## Run
Create a file called `.env` and place your Twitter App 's credentials as well your mongo connection string and your database info. Just like shown in the `.env-sample` file.
```
python src/app.py
```
Or run:
```
make run
```
Replace the terms inside the list `TRACK` defined in `app.py`with the ones you want to track. 

## Build docker image
```
make docker_build
```
## Run docker image
```
make docker_run
```
