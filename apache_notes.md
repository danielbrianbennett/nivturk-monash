## Apache notes

### Access

``` ssh dben0009@mnhs-web170-v01.ocio.monash.edu```

or

``` ssh dben0009@psychtest.med.monash.edu```

### Website

- Main alias is ```https://psychtest.med.monash.edu```


### Apache
- Main website files appear to be in ```/var/www/html```
- Main config file is ```/etc/httpd/conf/httpd.conf```
- Additional SSL config at ```/etc/httpd/conf.d/ssl.conf```
- Additional config files located at ```/etc/httpd/conf.d```
- Check Apache status with ```systemctl status httpd.service```
- Start/stop/restart server with ```systemctl <start/stop/restart> httpd.service```
- Config files for loading additional modules are at ```/etc/httpd/conf.modules.d/```

### Installing mod_wsgi

Instructions from https://modwsgi.readthedocs.io/en/develop/user-guides/quick-installation-guide.html and https://httpd.apache.org/docs/2.4/programs/apxs.html

All of the below follows ```sudo sudosh```

Running into issues with different Python distributions. For python3, just used ```pip install mod_wsgi```


### New process

```
source activate nivturk

pip install mod_wsgi-express

# get configuration details, to be put into httpd. (see https://pypi.org/project/mod-wsgi/)
mod_wsgi-express module-config
```

Check running process with ``` httpd -t -D DUMP_INCLUDES```

### My process

Assumes that the ssl.conf file has been updated with redirects, e.g.,

```

#####################
# Task setup block
#####################

## Task 1: Nivturk demo

# Reverse proxy configuration
<Location /nivturk_demo/>

        ProxyPass http://localhost:9000/
        ProxyPassReverse http://localhost:9000/

</Location>

# Rewrite URL to add a trailing slash (for Flask)
RewriteEngine on
RewriteRule ^/nivturk_demo$ /nivturk_demo/ [R]

## Task 2: Flask hello world demo

# Reverse proxy configuration
<Location /flask_hello_world/>

        ProxyPass http://localhost:9001/
        ProxyPassReverse http://localhost:9001/

</Location>

# Rewrite URL to add a trailing slash (for Flask)
RewriteEngine on
RewriteRule ^/flask_hello_world$ /flask_hello_world/ [R]
```

To set this up:

``` bash

# create detached window
tmux

# launch virtual environment
source activate nivturk

# launch gunicorn
gunicorn -b 0.0.0.0:<port-number> -w 4 app:app

# detach session with Ctrl-b, followed by d

```
