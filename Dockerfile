FROM python:3.7-buster

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qqy && apt-get install -qqy \
  make \
  clang \
  curl \
  gcc \
  g++

RUN python3.7 -m pip install numpy pandas scipy pytest

RUN touch newfile.txt

