FROM python:3.8
WORKDIR /usof
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
ENV PYTHONUNBUFFERED 1
CMD ["python", "start_server.py"]
