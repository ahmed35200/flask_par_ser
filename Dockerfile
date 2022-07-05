FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y redis-server && \
    apt-get clean
RUN apt-get update && apt-get install -y python3.9 python3-pip
RUN apt-get install ffmpeg libsm6 libxext6  -y
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install --upgrade pip
RUN pip install --default-timeout=100 future

RUN pip3 install -r requirements.txt
COPY . /app
CMD [ "python3", "./app.py" ]
