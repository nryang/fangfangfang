FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY . /fangfangfang
WORKDIR /fangfangfang

RUN python3 setup.py install
