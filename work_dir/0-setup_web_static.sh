#!/usr/bin/env bash
#a bashscript that set up my web servwes for the deployment of webstatic

#updating the our machine and installing nginx
sudo apt-get update
sudo apt-get install -y nginx

#starting to create web folders to store our dats
sudo service nginx start
mkdir -p /data/
mkdir -p /data/web_static
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test/
echo 'Mastermose is the best, The lord God of Moses and Joshua is with him
	unquenchable
	A more than conqueror, conquering along his path
	inexorable and unshakeable
	Blessed be the lord God of Moses
	' > /data/web_static/releases/test/index.html

#forefully creating a symbolic link every time this script is run
ln -sf /data/web_static/releases/test/ /data/web_static/current

#recursively given permission to specified user and group
sudo chown -R ubuntu:ubuntu /data/

printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	root /var/www/html;
	index index.html index.htm;

	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}

	location /redirect_me {
		return 303 https://www.youtube.com;
	}

	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}" > /etc/nginx/sites-available/default

sudo service nginx restart
