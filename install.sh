#!/bin/sh

curl -sSL https://get.docker.com/ | sh
# Replace <your_user> with your username
sudo usermod -aG docker `whoami`
sudo apt-get install -y python
sudo apt-get install -y docker-compose
