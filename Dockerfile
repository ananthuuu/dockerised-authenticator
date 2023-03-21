FROM python:3.9-slim-buster
RUN apt-get update && apt-get install -yq wget gnupg curl unzip libcurl4
RUN apt-get update && apt --fix-broken install -yq


RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# Install Chrome
RUN apt install -yq libcurl4

RUN dpkg -i google-chrome-stable_current_amd64.deb || apt --fix-broken install -yq

# Install Chrome driver
RUN version=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget https://chromedriver.storage.googleapis.com/$version/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chown root:root /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver


# Copy the requirements file into the container
COPY requirements.txt .
COPY app.py .
COPY test.py .
# Install the necessary packages
RUN pip install --no-cache-dir -r requirements.txt


# Start the applicationcd app
CMD ["python", "test.py"]