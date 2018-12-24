FROM python:3.6-alpine

RUN adduser -D gear_compare

WORKDIR /home/gear_compare

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY gear_compare.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP gear_compare.py

RUN chown -R gear_compare:gear_compare ./
USER gear_compare

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
