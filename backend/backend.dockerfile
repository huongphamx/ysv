FROM python:3.11-slim

WORKDIR /app/

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . .
RUN chmod +x ./start.sh

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["/app/start.sh"]
