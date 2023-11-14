# Dockerfile
FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY cli.py .

CMD ["python", "cli.py"]
