### 8. Dockerfile (same for all services)

FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask prometheus_client requests
CMD ["python", "main.py"]
