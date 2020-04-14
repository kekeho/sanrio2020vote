FROM python:3.8

WORKDIR /code
COPY ./requirements.txt /code
RUN pip install -r requirements.txt

COPY ./sanrioVote.py /code
COPY ./vote.json /code

CMD [ "python", "sanrioVote.py" ]
