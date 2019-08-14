FROM python:3.7.3

WORKDIR /usr/src/app

COPY django ./
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "sample.wsgi", "--bind=0:8000"]
