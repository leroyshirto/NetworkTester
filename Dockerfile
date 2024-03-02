FROM python:3.13.0a4-slim

EXPOSE 5000

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY app.py /app
COPY config.py /app


ENTRYPOINT ["python"]

CMD ["app.py"]
