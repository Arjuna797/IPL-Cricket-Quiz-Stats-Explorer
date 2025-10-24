# Use an official Python runtime as a parent image
# Using python:3.10-slim as a lightweight and stable base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code and data into the container
# This assumes your CSV is in a folder named "IPL Matches 2008-2020.csv"
COPY . .

# Make port 8501 (Streamlit's default port) available
EXPOSE 8501

# Set Streamlit-specific environment variables for running in a container
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLE_CORS=false

# The command to run your Streamlit app
# Assumes your main script is named "IPL_Streamlit_App.py"
CMD ["streamlit", "run", "IPL_Streamlit_App.py"]
