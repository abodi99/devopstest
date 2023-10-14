# Use the Python 3.8 base image from Docker Hub
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the Calculator application files into the container§
COPY . .
#COPY requirements.txt /app/

# Install the Python dependencies specified in requirements.txt
RUN pip install -r ./requirements.txt

# Set the ENTRYPOINT to run the calculator.py script
ENTRYPOINT ["python", "calculator.py"]