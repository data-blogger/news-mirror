FROM python:3.9.0-alpine
WORKDIR /project
COPY requirements.txt /project/requirements.txt
RUN pip install -r requirements.txt
ADD . /project
ENV FLASK_APP=server
ENV FLASK_ENV=development
CMD ["python", "server.py"]