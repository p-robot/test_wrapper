FROM python:3.7-buster
ENV DEBIAN_FRONTEND noninteractive
RUN python3.7 -m pip install numpy pandas scipy
