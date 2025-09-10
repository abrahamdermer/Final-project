FROM python:3.11-slim

WORKDIR /app
COPY  ..Preprocessing /app/
COPY ..requirements.txt /app/
COPY ..tools /app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.Preprocessing.manager"]

