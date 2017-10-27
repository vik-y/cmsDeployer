import os, sys, string, random
from config import *


# TODO: Add argparse or optparse

def generatePassword():
    n = 12
    password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
    return password

def create_db(dbname, user, password):
    cmd ="""docker exec -it mysqldb mysql -u root -p%s --execute="CREATE DATABASE %s;
    USE %s;
    GRANT ALL PRIVILEGES ON *.* TO '%s'@'%%' IDENTIFIED BY '%s';\"""" % (ROOT_PASSWORD,dbname, dbname, user, password)
    print cmd
    os.system(cmd)

def get_compose_file(sitename, dbname, user, password, vhost):
    fl="""
wordpress:
    image: wordpress:latest # https://hub.docker.com/_/wordpress/
    volumes:
      - ./config/php.conf.uploads.ini:/usr/local/etc/php/conf.d/uploads.ini
      - ./wp-app:/var/www/html:z # Full wordpress project
      #- ./plugin-name/trunk/:/var/www/html/wp-content/plugins/plugin-name # Plugin development
      #- ./theme-name/trunk/:/var/www/html/wp-content/themes/theme-name # Theme development
    environment:
      VIRTUAL_HOST: %s
      WORDPRESS_DB_HOST: mysqldb
      WORDPRESS_DB_NAME: %s
      WORDPRESS_DB_USER: %s
      WORDPRESS_DB_PASSWORD: %s
    external_links:
      - mysqldb
    restart: always
    container_name: %s_wordpress
""" % (vhost, dbname, user, password, sitename)
    print fl
    return fl

sitename = sys.argv[1]
dbname = sitename
uname = sitename
password = generatePassword()
vhost = sys.argv[2]

create_db(dbname, uname, password)
#create_compose_file("site", "dbname", "user", "password", "sitename.iiitb.org")
os.system("mkdir %s" % sitename)
with open("%s/docker-compose.yml" % sitename, "w") as f:
    f.write(get_compose_file(sitename, dbname, uname, password, vhost))
os.system("cd %s && docker-compose up -d" % sitename)
