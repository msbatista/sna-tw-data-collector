# sna-tw-data-collector

## Introduction
A very simple wrapper around `Tweepy` to track twitter data and insert into a mongodb collection.

## Instalation
```
python3.6 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
Create a file called `.env` and place your Twitter App 's credentials as well your mongo connection string and your database info. Just like shown in the `.env-sample` file.
```
python src/app.py
```
Replace the terms inside the list `TRACK` defined in `app.py`with the ones you want to track. 


