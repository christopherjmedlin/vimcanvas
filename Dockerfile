FROM python:3.6

MAINTAINER Christopher Medlin <christopherjmedlin@gmail.com>

RUN mkdir /opt/vimcanvas
WORKDIR /opt/vimcanvas
ADD requirements.txt /opt/vimcanvas/
RUN pip3 install -r requirements.txt
ADD . /opt/vimcanvas