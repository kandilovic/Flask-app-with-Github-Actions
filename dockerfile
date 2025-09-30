FROM python:3.9-slim


# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy source code
COPY . .


# Set environment variables (can be overridden by Docker Compose)
ENV DB_HOST=db
ENV DB_NAME=mydb
ENV DB_USER=user
ENV DB_PASS=password


CMD ["python", "app.py"]