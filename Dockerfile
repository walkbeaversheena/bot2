FROM ubuntu:latest

RUN apt-get update && apt-get install python3 python3-pip ipython3 && pip install -U aiogram

RUN apt-get install -y nano 

