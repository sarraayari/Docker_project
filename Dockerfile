# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /Docker_project

# Copy the current directory contents into the container at /app
COPY . /Docker_project

# Install any needed packages specified in requirements.txt
RUN chown -R  pip install -r requirements.txt

# Expose the ports for Flask services
EXPOSE 5001
EXPOSE 5002

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run Flask services

CMD ["flask", "run", "--port=5001"]  #For SVM-based
#uncomment the line below to switch services
#CMD ["flask", "run", "--port=5002"]  #For VGG19-based


CMD ["python", "app.py"]
