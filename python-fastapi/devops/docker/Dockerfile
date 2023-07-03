FROM python:3.11.2-slim-bullseye

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY ./requirements/docker.txt /requirements.txt

RUN pip install -U pip && \
    pip install --no-cache-dir --prefer-binary -r /requirements.txt

WORKDIR /app

COPY ./service /app/service

CMD ["uvicorn", "service.main:app", "--host", "0.0.0.0", "--port", "8000"]