#!/usr/bin/env bash
# Nginx web server setup script for static web content deployment.
#
# This script automates the installation and configuration of Nginx to serve
# static web content from a custom directory structure. It creates the necessary
# directory hierarchy, sets up a test HTML page, configures Nginx with a custom
# server block, and establishes proper file permissions.

if ! dpkg -s nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/

sudo mkdir -p /data/web_static/shared/

sudo mkdir -p /data/web_static/releases/test/

HTML_CONTENT="<html>\n  <head>\n  </head>\n  <body>\n    ALX\n  </body>\n</html>"
echo -e "$HTML_CONTENT" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

printf %s "#

# Default server configuration
#
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    add_header X-Served-By $HOSTNAME;
    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

}

#" > /etc/nginx/sites-available/default


# Restart the Nginx service to apply the new configuration
# Uses systemctl for service management on systemd-based systems
sudo systemctl restart nginx
