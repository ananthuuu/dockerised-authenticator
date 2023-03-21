
#installing chrome binary
apt-get update && apt-get install -yq wget gnupg curl unzip
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install libcurl4
apt --fix-broken install
dpkg -i google-chrome-stable_current_amd64.debdpkg -s google-chrome-stable
dpkg -s google-chrome-stable

#installing chrome driver
version=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget https://chromedriver.storage.googleapis.com/$version/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin/chromedriver
chown root:root /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver