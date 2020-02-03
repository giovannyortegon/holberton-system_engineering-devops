#!/usr/bin/env bash
# Install Nginx web server

exec {
    command    => 'sudo apt-get -y update && sudo apt-get -y install nginx && echo "Holberton School" > /var/www/html/index.nginx-debian.html && redirect="\\\trewrite ^/redirect_me 301 https://34.74.157.171 permanent;" && sudo sed -i "20i listen 443 ssl" && sudo sed -i "42i $redirect" /etc/nginx/sites-available/default && sudo service nginx start',
	provider   => shell,
}
