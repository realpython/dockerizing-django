FROM python:3.6.5-stretch

RUN groupadd -r django && useradd -r -m -g django django
ENV PATH="/home/django/.local/bin:${PATH}"
USER django:django

WORKDIR /home/django/app
COPY requirements.txt /home/django/app
RUN pip install --user --no-cache-dir -r requirements.txt
COPY . /home/django/app
