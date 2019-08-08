FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN apt-get update

# Update to the latest pip
RUN pip3 install --upgrade pip

# If STATIC_INDEX is 1, serve / with /static/index.html directly (or the static URL configured)
ENV STATIC_INDEX 1

COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY ./app /app

WORKDIR /app
