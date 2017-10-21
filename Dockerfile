FROM python:3.6-jessie
RUN apt-get update
RUN apt-get install -y build-essential libssl-dev  g++ \
    libblas-dev liblapack-dev libopenblas-dev gfortran libxml2-dev zlib1g-dev \
    libxslt1-dev locales-all gcc curl

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --upgrade -r requirements.txt

COPY . /usr/src/app

ENTRYPOINT ["deploy/sh_scripts/entrypoint.sh"]
