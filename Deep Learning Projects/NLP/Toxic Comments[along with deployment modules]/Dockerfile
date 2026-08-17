FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt toxic_comments_model.pkl app.py ./
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "app.py"]
