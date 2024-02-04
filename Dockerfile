FROM python:3.11

RUN apt update && apt-get -y install libc-dev build-essential

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY . .
