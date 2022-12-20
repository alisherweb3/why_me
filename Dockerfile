# The FROM instruction specifies the Parent Image from which you are building
FROM python:3.10

# Environment variables
# Prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED=1

# The working directory of a Docker container
WORKDIR /why_me

# Copying and running files to the why_me directory
COPY requirements.txt /why_me/requirements.txt
RUN pip install -r requirements.txt

# Comunication port for API's
# EXPOSE 8000