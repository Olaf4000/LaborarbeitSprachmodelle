FROM python:3.9
WORKDIR /FlaskApp
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "-m",  "flask", "run", "--host=0.0.0.0"]