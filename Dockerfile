# Set up base environment
FROM python:3.11

# Expose Ports

EXPOSE 80

RUN /usr/local/bin/python -m pip install --upgrade pip

# Set working directory
WORKDIR /app

#Install Requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy Files to container image
COPY . .

ENV OAUTHLIB_INSECURE_TRANSPORT=1
ENV OAUTHLIB_RELAX_TOKEN_SCOPE=1
# Run the app
# CMD ["python", "run.py"]
CMD exec gunicorn --bind 0.0.0.0:80 --workers 4 --threads 8 -t 0 "app:app"