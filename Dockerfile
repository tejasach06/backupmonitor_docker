FROM alpine:3

# Install required packages
RUN apk add --no-cache \
    musl-dev \
    gcc \
    mariadb-dev \
    python3-dev

RUN apk add --no-cache python3 py3-pip py3-gunicorn

# Copy the Flask application code and requirements.txt file
COPY app /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app

# Create a virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Set environment variables
ENV FLASK_APP=main.py
ENV FLASK_ENV=production

# Start the Flask application with Gunicorn
CMD gunicorn -b 0.0.0.0:8000 --access-logfile - --error-logfile - main:app