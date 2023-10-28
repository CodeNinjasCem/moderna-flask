FROM python:3.9.1
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python", "servidor.py"]

# docker build -t myflaskapp .
# docker run -p 8003:8083 myflaskapp