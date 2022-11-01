# Dockerfile, Image, Container

FROM python:3.8

WORKDIR /app

COPY api.py .

#install pip 
RUN pip install requests 

CMD ["python", "./api.py"]


