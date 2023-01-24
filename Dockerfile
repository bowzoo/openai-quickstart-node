FROM python:3.8-slim-buster


WORKDIR /openai-quickstart-python

COPY . .

RUN pwd

RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt

# flask defualt ip: 127.0.0.1 and port: 5000
ENTRYPOINT ["flask", "run"]
#CMD ["-h", "0.0.0.0", "-p", "5008"]
