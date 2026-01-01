FROM python:3.12
WORKDIR /personal-flask-blog

#Install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#Copy everything over
COPY . .
EXPOSE 8080
EXPOSE 5000

#Command to run
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]