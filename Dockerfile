FROM python:3.9

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app

COPY data_preprocessing.py .
#COPY input_data.json .