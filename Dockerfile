FROM python:3.8-alpine3.14

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --upgrade

COPY . .

EXPOSE 5050

CMD [ "python", "./app.py" ]