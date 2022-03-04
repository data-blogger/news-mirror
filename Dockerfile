FROM python:3.9.0-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
ENV FLASK_APP=server
ENV FLASK_ENV=development
CMD ["python", "server.py"]