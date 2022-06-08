# python:alpine is 3.{latest}
FROM python:alpine 

LABEL maintainer="Nobody"

RUN pip install flask redis

EXPOSE 5000

ENTRYPOINT ["python", "/app/app.py"]
