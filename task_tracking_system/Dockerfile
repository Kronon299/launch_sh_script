FROM python:3.8.6-buster

WORKDIR /app

# install and configure poetry for requirements version control
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY web_app/pyproject.toml web_app/poetry.lock ./

RUN poetry install --no-interaction --no-ansi

# Expose project services
EXPOSE 5000

COPY web_app .

CMD ["python", "main.py"]