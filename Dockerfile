FROM python:3.6-slim

RUN useradd -r -d /app py
WORKDIR /app
RUN chown -R py:py /app

RUN pip --no-cache-dir install pip --upgrade
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt

COPY src src
RUN chown -R py:py src

USER py
WORKDIR /app/src
EXPOSE 8080

ENTRYPOINT ["python", "./main.py"]
