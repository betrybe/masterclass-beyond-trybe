FROM python:3.9-alpine

WORKDIR /app

RUN adduser -D static
USER static

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
