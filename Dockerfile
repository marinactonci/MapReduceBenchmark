FROM python:3.8

WORKDIR /app

COPY mapReduceNP.py mapReduceP.py ./

RUN pip install pandas faker

CMD python mapReduceNP.py && python mapReduceP.py