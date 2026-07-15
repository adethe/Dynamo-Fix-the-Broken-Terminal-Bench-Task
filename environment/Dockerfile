FROM python:3.11-slim@sha256:63773ee99f2bde641a953a696be8645e7f1cbaf5285773663a43693f41ee1f86

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log

