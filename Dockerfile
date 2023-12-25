FROM python:3.8

WORKDIR /app

COPY ./main/. ./

RUN pip install pandas faker matplotlib

CMD python benchmark.py