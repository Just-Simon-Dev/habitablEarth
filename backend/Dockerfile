FROM python:3.10

WORKDIR /usr/src/app

COPY ./models/ ./models/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py"]