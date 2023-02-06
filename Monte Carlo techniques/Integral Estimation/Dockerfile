# syntax=docker/dockerfile:1

#The elegant method, in which we learn what activating actually does
#
#It’s easy to think of activate as some mysterious magic, a pentacle drawn in blood to keep Python safely trapped. But it’s just software, and fairly simple software at that. The virtualenv documentation will even tell you that activate is “purely a convenience.”
#
#If you go and read the code for activate, it does a number of things:
#
#It figures out what shell you’re running.
#It adds a deactivate function to your shell, and messes around with pydoc.
#It changes the shell prompt to include the virtualenv name.
#It unsets the PYTHONHOME environment variable, if someone happened to set it.
#It sets two environment variables: VIRTUAL_ENV and PATH.
#The first four are basically irrelevant to Docker usage, so that just leaves the last item. Most of the time VIRTUAL_ENV has no effect, but some tools—e.g. the poetry packaging tool—use it to detect whether you’re running inside a virtualenv.
#
#The most important part is setting PATH: PATH is a list of directories which are searched for commands to run. activate simply adds the virtualenv’s bin/ directory to the start of the list.
#
#We can replace activate by setting the appropriate environment variables: Docker’s ENV command applies both subsequent RUNs as well as to the CMD.
#
#The result is the following Dockerfile:

# reference: https://pythonspeed.com/articles/activate-virtualenv-dockerfile/

FROM python:latest

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD . /app
WORKDIR /app

# Install dependencies:
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Run the application:
COPY integral_estimation.py /app
CMD [ "python", "integral_estimation.py"]