# Example for substation_service
FROM python:3.10
WORKDIR /app
COPY main.py .
RUN pip install flask prometheus_client requests
CMD ["python", "main.py"]
