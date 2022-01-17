FROM python:3.8

WORKDIR /job_app

COPY ./requirements.txt /job_app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /job_app/requirements.txt

COPY ./app /job_app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"] 