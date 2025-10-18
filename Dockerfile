FROM python:3.9-slim
WORKDIR /app

# copy project files and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

# expose port 5000
EXPOSE 5000

# set environment variables
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

# run app
CMD ["python", "app.py"]
