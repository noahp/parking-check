FROM ubuntu:bionic

RUN apt-get update && apt-get install -y \
    curl \
    python \
    python-pip

RUN pip install \
    click

COPY sendmail.py /usr/local/bin/sendmail
COPY check-parking.sh /usr/local/bin/check-parking
