FROM python:3.9.2
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
#temporary
RUN apt-get update && apt-get install -y gettext
RUN useradd -m app
USER app
WORKDIR /code
COPY --chown=app:app requirements/base.txt requirements/dev.txt requirements/test.txt /code/requirements/
ENV PATH="/home/app/.local/bin:${PATH}"
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements/base.txt \
    && pip install -r requirements/dev.txt \
    && pip install -r requirements/test.txt
ADD --chown=app:app . /code/