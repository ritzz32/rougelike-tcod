FROM python:3.7.3

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
  build-essential \
  python3-dev \
  python3-numpy \
  libsdl2-dev \
  libffi-dev \
  libomp5

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
