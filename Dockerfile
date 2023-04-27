FROM python:3.10.9-slim-bullseye
LABEL authors="Jonggwan Park <craftguy55@gmail.com>"
LABEL description="Dockerfile for building a Python 3.10.9 image with pipenv"
LABEL version="1.0.0"

WORKDIR /back
#ENV PYTHONUNBUFFERED=1
#ENV PYTHONPATH=/back

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 443

ENTRYPOINT ["python", "/back/main.py"]

