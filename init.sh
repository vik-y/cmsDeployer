#!/bin/bash

# This script takes care of running all the necessary images like
# mysql, phpmyadmin and portainer

# Run reverse proxy
# This will help in routing request to the appropriate containers
docker run -d -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro jwilder/nginx-proxy

# Start mysql and phpmyadmin
cd mysql && docker-compose up -d
