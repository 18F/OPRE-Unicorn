FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get clean && rm -rf /var/lib/apt/lists/*
ENV DJANGO_SETTINGS_MODULE=opre_ops.settings.local
WORKDIR /opre_project
COPY ./backend/Pipfile ./backend/Pipfile.lock /opre_project/
RUN pip install --no-cache-dir --upgrade pip==22.2 pipenv==2022.7.24 && pipenv install --dev --system --deploy
COPY ./backend/opre_ops/ /opre_project/
