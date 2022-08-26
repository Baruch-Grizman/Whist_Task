# using python slim from docker hub
FROM python:slim
# work dir for our application
WORKDIR /app
# copy all files
COPY . .
# install requirements for our application
RUN pip install -r requirements.txt
# run application mapped to port 9090
CMD gunicorn --bind 0.0.0.0:9090 flasklocalip:app
