FROM python:latest
WORKDIR  /app
ENV PYTHONUNBUFFERED=1
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN python3 manage.py migrate --run-syncdb

CMD ["python3", "manage.py","runserver", "0.0.0.0:8000"]