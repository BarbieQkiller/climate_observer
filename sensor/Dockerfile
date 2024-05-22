FROM python:3.12-bookworm

RUN pip install requests

COPY sensor.py /

ENTRYPOINT ["python", "/sensor.py"]
