FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd --create-home --uid 10001 study

COPY --chown=study:study learning ./learning
COPY --chown=study:study practice ./practice

USER study

EXPOSE 8765

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python3 -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8765/api/content').read(1)"

CMD ["python3", "learning/study/serve.py", "--host", "0.0.0.0", "--port", "8765"]
