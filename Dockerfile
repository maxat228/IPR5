FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local

COPY src/ ./src/
COPY server.py ./
COPY requirements.txt .

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080
CMD ["python", "server.py"]

LABEL maintainer="Ваше Имя <ваш.email@example.com>"
LABEL version="2.0.0"
LABEL description="Калькулятор с CI/CD пайплайном и HTTP API"