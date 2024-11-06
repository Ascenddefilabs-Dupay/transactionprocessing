
FROM python:3.11-slim

WORKDIR /backend-transaction-processing

COPY requirements.txt /backend-transaction-processing/
RUN pip3 install -r /backend-transaction-processing/requirements.txt
COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8009"]
