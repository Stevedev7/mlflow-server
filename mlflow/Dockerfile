
FROM python:3.8-slim

RUN python -m pip install --upgrade pip

RUN pip install cryptography google-cloud-storage mlflow boto3 pymysql gcsfs fsspec

WORKDIR /dir

COPY ./ ./

ENV GOOGLE_APPLICATION_CREDENTIALS=/dir/cred.json

RUN mkdir artifacts

EXPOSE 5000