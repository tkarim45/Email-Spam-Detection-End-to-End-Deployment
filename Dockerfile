FROM python:3.9.18 

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080 

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]docker ps
