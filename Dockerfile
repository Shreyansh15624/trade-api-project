# Using the official light-weight python version for lower load on Server Computing
FROM python:3.12-slim

# Creating the woking directory for the project
WORKDIR /marketintel

# We copy ONLY the requirements first
COPY requirements.txt .

# Installing the Python Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying the backed code (The .dockerignore will automatically block the listed folders here)
COPY . .

# Exposing the Port FastAPI runs on
EXPOSE 8000

# Starting the Server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]