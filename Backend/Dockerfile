# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install Flask and Jinja2 packages
RUN pip install  Flask==1.1.2 Jinja2==2.11.3
RUN pip install --upgrade flask
RUN pip install flask_cors
# Make port 80 available to the world outside this container
EXPOSE 8000
# Run app.py when the container launches
CMD ["python", "app.py"]
