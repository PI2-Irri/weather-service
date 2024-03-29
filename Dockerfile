FROM python:3.6

RUN apt-get update && \
    apt-get install -y cron

WORKDIR /weather-service

COPY . /weather-service

# Setting cron
COPY crons/cronjob /etc/cron.d/weathercron

RUN chmod 0644 /etc/cron.d/weathercron

RUN touch /var/log/cron.log

RUN /usr/bin/crontab /etc/cron.d/weathercron

RUN pip install --no-cache-dir -r requirements.txt
