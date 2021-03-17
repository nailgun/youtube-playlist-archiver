FROM python:3.9

ENV PYTHONUNBUFFERED=1
ENV DEV_ENV=no

RUN pip install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN SECRET_KEY=build ./manage.py collectstatic

ENTRYPOINT ["./manage.py"]
