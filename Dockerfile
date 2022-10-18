FROM python:3.6.12-alpine
COPY requirements.txt .
RUN apk update && apk add --no-cache supervisor
RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app
RUN chmod +x ./gunicorn.sh
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
