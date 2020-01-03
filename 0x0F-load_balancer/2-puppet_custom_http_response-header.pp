#!/usr/bin/env bash
# Install Nginx

exec {'Install nginx':
  command => 'sudo apt-get update && sudo apt-get -y install nginx && sudo sed -i "15i add_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.cfg && sudo service nginx restart',
    provider => shell,
    }
