FROM python:3.10

WORKDIR /usr/src/app

COPY ./backend/models/ ./models/

COPY ./backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend .
COPY /data/certs/ ./

CMD [ "python", "app.py"]