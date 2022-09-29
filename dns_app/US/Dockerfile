FROM python:3.5

# Set up a working folder and install the pre-reqs
WORKDIR /app

RUN pip install Flask

COPY --chown=nyu:nyu . .

CMD [ "python", "./run.py" ]
